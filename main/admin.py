from django.contrib import admin

from django.contrib.flatpages.models import FlatPage
from redactor.widgets import RedactorEditor
from modeltranslation.admin import TranslationAdmin
from  flatblocks.models import FlatBlock
from  flatblocks.forms import FlatBlockForm


from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from hijack_admin.admin import HijackUserAdminMixin



class CustomUserAdmin(UserAdmin,HijackUserAdminMixin):
    list_display = UserAdmin.list_display + ('hijack_field',)

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
