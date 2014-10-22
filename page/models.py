# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Page(models.Model):
    title = models.CharField(max_length=250, verbose_name=_(u'Title'))
    content = models.TextField(blank=True)
    seo_content = models.TextField(verbose_name=_(u'МЕТА content'))
    seo_title =   models.TextField(verbose_name=_(u'МЕТА title'))
    seo_keywords = models.TextField(verbose_name=_(u'МЕТА keywords'))
    slug = models.CharField(max_length=250, verbose_name=_(u'Slug'),blank=True)
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Pages' 
        verbose_name = 'Page'
