from django import template
from catalog.models import Journal
register = template.Library()

@register.inclusion_tag("catalog/in_tags.html")
def new_pressa_tag():
    out = {}
    c = Journal.objects.all().order_by(in_popular_pressa=True)
    out['items'] = c
    out['class'] = 'new_pressa_tag'
    return out


