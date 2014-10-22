#-*- coding: utf-8 -*-
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from page.models import Page
register = template.Library()
@register.filter(name='get_page')
@stringfilter
def get_page(value):
    try:
        page = Page.objects.get(slug=value)
    except:
        return 'page '+str(value)+' not found'
    return mark_safe(page.content)
