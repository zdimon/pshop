from django.contrib import admin
from catalog.models import Catalog, Journal, Issue, Purchase, CurrencyHistory, ImportLog
from mptt.admin import MPTTModelAdmin
from django import forms
from redactor.widgets import RedactorEditor
from modeltranslation.admin import TranslationAdmin
from paymaster.models import Payment
from django.http import HttpResponse
from django.conf.urls import patterns






class CatalogAdmin(MPTTModelAdmin,TranslationAdmin):
    list_filter = ('category_type', )
    list_display = ( 'name', 'category_type', 'sorting')
    list_editable = ['sorting']
    ordering = ('-sorting',)


admin.site.register(Catalog, CatalogAdmin)


class JournalAdminForm(forms.ModelForm):
    class Meta:
        model = Journal
        widgets = {
           'description_hy': RedactorEditor(),
           'description_ru': RedactorEditor(),
           'description_en': RedactorEditor(),
        }


class JournalAdmin(TranslationAdmin):
    list_display = ( 'name', 'get_cover', 'price', 'price_dram', 'price_usd', 'recount' )
    list_filter = ('journal_type', )
    search_fields = ['name_ru', 'name_hy', 'name_en']
    list_editable = [ 'price', 'price_dram', 'price_usd']
    list_display_links = ['name']
    form = JournalAdminForm


admin.site.register(Journal, JournalAdmin)


class IssueAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'get_cover',  'journal', 'date' )
    list_filter = ('date',)
    search_fields = ['name']


admin.site.register(Issue, IssueAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'issue', 'price', 'created' )


admin.site.register(Purchase, PurchaseAdmin)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ( 'date', 'rub2dram', 'dram2usd', 'my_link' )
    
    def my_link(self, obj):
        return '<a href="/admin/recount/%s">%s</a>' % (obj.id, 'Recount')
    my_link.allow_tags = True




admin.site.register(CurrencyHistory, CurrencyAdmin)


class ImportLogAdmin(admin.ModelAdmin):
    list_display = ( 'journal', 'issue', 'created', 'is_imported')


admin.site.register(ImportLog, ImportLogAdmin)



class PaymentAdmin(admin.ModelAdmin):
    list_display = ( 'owner', 'ammount', 'operation_status', 'payment_num', 'datetime' )


admin.site.register(Payment, PaymentAdmin)


from catalog.tasks import recount_prices

def my_view(request,id):
    #import pdb; pdb.set_trace()
    h = CurrencyHistory.objects.get(pk=id)
    recount_prices.delay(h)
    return HttpResponse("Process started!")


def get_admin_urls(urls):
    def get_urls():
        my_urls = patterns('',
            (r'^recount/(?P<id>[-\w]+)$', admin.site.admin_view(my_view))
        )
        return my_urls + urls
    return get_urls
admin_urls = get_admin_urls(admin.site.get_urls())
admin.site.get_urls = admin_urls



