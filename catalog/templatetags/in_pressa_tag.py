from django import template
from catalog.models import Journal
register = template.Library()

@register.inclusion_tag("catalog/in_tags.html")
def in_pressa_tag():
    out = {}
    c = Journal.objects.filter(in_pressa=True).all()
    out['items'] = c
    out['class'] = 'in_pressa_tag'
    return out


