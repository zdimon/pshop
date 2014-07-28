# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import TreeForeignKey, MPTTModel

class Catalog(MPTTModel):
    JOURNAL_TYPE_CHOICES = (
        ('magazine', _(u'Journal')),
        ('paper', _(u'Paper')),
        ('book', _(u'Book')),
    )
    pub = models.BooleanField(verbose_name=_('Is published?'), default=False)
    name = models.CharField(verbose_name=_('Name'),max_length=250, blank=True)
    category_type = models.CharField(verbose_name=_(u'type of the publication'),
                                     choices=JOURNAL_TYPE_CHOICES,
                                     default='magazine',
                                     max_length=10)
    image = models.ImageField(verbose_name=_(u'image of the category'),
                              upload_to='catalog/%Y/%m/%d',
                              blank=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='sub_category')
    def __unicode__(self):
        return self.name
    class MPTTMeta:
        order_insertion_by = ['name']