from django.contrib import admin
from main.models import Catalog
class CatalogAdmin(admin.ModelAdmin):
    pass


admin.site.register(Catalog, CatalogAdmin)
