from django.contrib import admin
from catalog.models import Catalog, Journal, Issue
from mptt.admin import MPTTModelAdmin
class CatalogAdmin(MPTTModelAdmin):
    list_filter = ('category_type', )


admin.site.register(Catalog, CatalogAdmin)


class JournalAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'price', 'journal_type' )
    list_filter = ('journal_type', )


admin.site.register(Journal, JournalAdmin)


class IssueAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'journal', 'date' )
    list_filter = ('date',)
    search_fields = ['name']


admin.site.register(Issue, IssueAdmin)
