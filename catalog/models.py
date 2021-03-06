# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import TreeForeignKey, MPTTModel
import pytils
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

class Catalog(MPTTModel):
    JOURNAL_TYPE_CHOICES = (
        ('magazine', _(u'Journal')),
        ('paper', _(u'Paper')),
        ('book', _(u'Book')),
    )
    pub = models.BooleanField(verbose_name=_('Is published?'), default=False)
    name = models.CharField(verbose_name=_('Name'),max_length=250, blank=True)
    name_slug = models.CharField(verbose_name=_('Name slug'),max_length=250, blank=True)
    category_type = models.CharField(verbose_name=_(u'type of the publication'),
                                     choices=JOURNAL_TYPE_CHOICES,
                                     default='magazine',
                                     max_length=10)
    image = models.ImageField(verbose_name=_(u'image of the category'),
                              upload_to='catalog/%Y/%m/%d',
                              blank=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='sub_category')
    original_id = models.IntegerField(db_index=True, verbose_name=_('Original id'))
    def __unicode__(self):
        return self.name

    def save(self, **kwargs):
        self.name_slug = pytils.translit.slugify(self.name)
        return super(Catalog, self).save(**kwargs)

    def get_absolute_url(self):
       return reverse("catalog", kwargs={"slug": self.name_slug})

    class MPTTMeta:
        order_insertion_by = ['name']

class Journal(models.Model):
    JOURNAL_TYPE_CHOICES = (
        ('magazine', _(u'Журнал')),
        ('paper', _(u'Газета')),
        ('book', _(u'Книга')),
    )
    name = models.CharField(verbose_name=_('Name'),max_length=250, blank=True)
    name_slug = models.CharField(verbose_name=_('Name slug'),max_length=250, blank=True)
    description = models.TextField(verbose_name=_('Description'),max_length=250, blank=True)
    journal_type = models.CharField(verbose_name=_(u'type of journal (magazine, paper or book)'),
                                    choices=JOURNAL_TYPE_CHOICES,
                                    default='magazine',
                                    max_length=10)
    price = models.DecimalField( verbose_name=_('Price'), max_digits= 12, decimal_places= 2)
    cover = models.ImageField(upload_to='journal_cover', verbose_name=_('Journal cover'), blank=True)
    original_id = models.IntegerField(db_index=True, verbose_name=_('Original id'))
    category = models.ManyToManyField(Catalog,
                                      blank=True,
                                      verbose_name=_(u'Catalogs'))
    def save(self, **kwargs):
        self.name_slug = pytils.translit.slugify(self.name)
        return super(Journal, self).save(**kwargs)

    @property
    def get_cover(self):
        try:
            return mark_safe('<img src="%s" />' % self.cover.url)
        except:
            return mark_safe('<img src="%s" />' % '/media/journal_cover/plug.jpg')

    def get_absolute_url(self):
       return reverse("journal", kwargs={"slug": self.name_slug})

    def __unicode__(self):
        return self.name

class Issue(models.Model):
    journal =  models.ForeignKey(Journal, verbose_name=_('Journal'))
    cover = models.ImageField(upload_to='issue_cover', verbose_name=_('Issue cover'), blank=True)
    name = models.CharField(verbose_name=_('Name'),max_length=250, blank=True)
    date = models.DateTimeField(blank=True, null=True)
    original_id = models.IntegerField(db_index=True, verbose_name=_('Original id'))
    def __unicode__(self):
        return self.journal.name+u' номер '+self.name
    @property
    def get_cover(self):
        try:
            return mark_safe('<img src="%s" />' % self.cover.url)
        except:
            return ''

class Purchase(models.Model):
    issue =  models.ForeignKey(Issue, verbose_name=_('Issue'))
    user =   models.ForeignKey(User, verbose_name=_('User'))
    price = models.DecimalField( verbose_name=_('Price'), max_digits= 12, decimal_places= 2)
    created = models.DateTimeField(auto_now_add=True, auto_now=True, blank=True, null=True)