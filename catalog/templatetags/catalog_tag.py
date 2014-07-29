from django import template
from catalog.models import Catalog
register = template.Library()

@register.inclusion_tag("catalog/catalog.html")
def catalog_tag():
    out = {}
    c = Catalog.objects.all()
    out['items'] = c
    return out


