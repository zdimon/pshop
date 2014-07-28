from django.contrib import admin
from catalog.models import Catalog
from mptt.admin import MPTTModelAdmin
class CatalogAdmin(MPTTModelAdmin):
    list_filter = ('category_type', )


admin.site.register(Catalog, CatalogAdmin)
