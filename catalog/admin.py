from django.contrib import admin
from catalog.models import Catalog, Journal, Issue, Purchase, CurrencyHistory
from mptt.admin import MPTTModelAdmin
from django import forms
from redactor.widgets import RedactorEditor
from modeltranslation.admin import TranslationAdmin
from paymaster.models import Payment


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
    list_display = ( 'name', 'name_ru', 'name_hy', 'name_en', 'price', 'price_dram', 'price_usd', 'journal_type' )
    list_filter = ('journal_type', )
    search_fields = ['name_ru', 'name_hy', 'name_en']
    list_editable = [ 'name_ru', 'name_hy', 'name_en', 'price', 'price_dram', 'price_usd']
    list_display_links = ['name']
    form = JournalAdminForm


admin.site.register(Journal, JournalAdmin)


class IssueAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'journal', 'date' )
    list_filter = ('date',)
    search_fields = ['name']


admin.site.register(Issue, IssueAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'issue', 'price', 'created' )


admin.site.register(Purchase, PurchaseAdmin)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ( 'date', 'rub2dram', 'dram2usd' )


admin.site.register(CurrencyHistory, CurrencyAdmin)




class PaymentAdmin(admin.ModelAdmin):
    list_display = ( 'owner', 'ammount', 'operation_status', 'payment_num', 'datetime' )


admin.site.register(Payment, PaymentAdmin)
