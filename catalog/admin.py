from django.contrib import admin
from catalog.models import Catalog, Journal, Issue, Purchase
from mptt.admin import MPTTModelAdmin
from django import forms
from redactor.widgets import RedactorEditor
from modeltranslation.admin import TranslationAdmin

class CatalogAdmin(MPTTModelAdmin,TranslationAdmin):
    list_filter = ('category_type', )


admin.site.register(Catalog, CatalogAdmin)


class JournalAdminForm(forms.ModelForm):
    class Meta:
        model = Journal
        widgets = {
           'description_ar': RedactorEditor(),
           'description_ru': RedactorEditor(),
        }


class JournalAdmin(TranslationAdmin):
    list_display = ( 'name', 'price', 'journal_type' )
    list_filter = ('journal_type', )
    search_fields = ['name', 'name_ru', 'name_ar']
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
