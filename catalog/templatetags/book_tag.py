from django import template
from catalog.models import Journal
register = template.Library()

@register.inclusion_tag("catalog/in_tags.html")
def book_tag():
    out = {}
    c = Journal.objects.filter(journal_type='book').all()
    out['items'] = c
    out['class'] = 'in_armenian_tag'
    return out

