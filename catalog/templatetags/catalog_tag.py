# -*- coding: utf-8 -*-
from django import template
from catalog.models import Catalog
register = template.Library()
from django.utils.translation import ugettext as _

@register.inclusion_tag("catalog/catalog.html")
def catalog_tag(t='paper'):
    out = {}
    c = Catalog.objects.filter(category_type=t).order_by('sorting')
    out['items'] = c
    if t == 'journal':
        out['title'] = _(u'Журналы')
    if t == 'paper':
        out['title'] = _(u'Газеты')
    if t == 'book':
        out['title'] = _(u'Книги')
    return out


