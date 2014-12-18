from django import template
from catalog.models import Journal
register = template.Library()

@register.inclusion_tag("catalog/in_tags.html")
def in_daily_tag():
    out = {}
    c = Journal.objects.filter(in_everyday=True).all()
    out['items'] = c
    out['class'] = 'in_daily_tag'
    return out


