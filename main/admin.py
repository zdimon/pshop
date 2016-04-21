from django.contrib import admin

from django.contrib.flatpages.models import FlatPage
from redactor.widgets import RedactorEditor
from modeltranslation.admin import TranslationAdmin
from  flatblocks.models import FlatBlock
from  flatblocks.forms import FlatBlockForm


from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from hijack_admin.admin import HijackUserAdminMixin
from django.core.urlresolvers import reverse
from django.conf.urls import patterns, url
from django.contrib import messages
from django.shortcuts import redirect
from catalog.tasks import reg
 
class CustomUserAdmin(UserAdmin,HijackUserAdminMixin):
    list_display = UserAdmin.list_display + ('hijack_field', 'export_user_link')

    def export_user_link(self, instance):
        if instance.id is None:
            return ''
        url = reverse('admin:export_user', args=[instance.id])
        return u'<a href="{0}">{1}</a>'.format(url, u'export to pressa')
    export_user_link.allow_tags = True

    def get_urls(self):
        urls = super(CustomUserAdmin, self).get_urls()
        admin_urls = patterns(
            '',
            url(r'^export_user/(?P<user_id>\d+)$',
                admin.site.admin_view(export_user),
                name="export_user"),
            
        )
        return admin_urls + urls

def export_user(request, user_id):
    user = User.objects.get(pk=user_id)
    reg.delay(user)
    messages.success(request, 'Export is runing!')
    return redirect(reverse('admin:auth_user_changelist')) # journal - application, issue - model



admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)




class MyFlatblocksForm(FlatBlockForm):
    class Meta:
        widgets = {
           'content_ar': RedactorEditor(),
           'content_ru': RedactorEditor(),
        }

class MyFlatBlockAdmin(TranslationAdmin):
    form = MyFlatblocksForm

admin.site.unregister(FlatBlock)
admin.site.register(FlatBlock, MyFlatBlockAdmin)
