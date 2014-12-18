from django import template
from catalog.models import Journal
register = template.Library()

@register.inclusion_tag("catalog/in_tags.html")
def new_pressa_tag():
    out = {}
    c = Journal.objects.all().order_by('-last_issue_id')[0:10]
    out['items'] = c
    out['class'] = 'new_pressa_tag'
    return out


