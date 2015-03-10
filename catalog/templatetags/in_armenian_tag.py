from django import template
from catalog.models import Journal
register = template.Library()

@register.inclusion_tag("catalog/in_tags.html")
def in_armenian_tag():
    out = {}
    c = Journal.objects.filter(in_am=True).all()
    out['items'] = c
    out['class'] = 'in_armenian_tag'
    return out


