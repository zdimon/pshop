# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import TreeForeignKey, MPTTModel
import pytils
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from redactor.fields import RedactorField
from catalog.tasks import reg 
from django.dispatch import receiver
from django.db.models.signals import post_save
from registration.models import RegistrationProfile
from registration.signals import user_activated 


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
    sorting = models.PositiveIntegerField(verbose_name=_(u'сортировка'))
    def __unicode__(self):
        return self.name

    def save(self, **kwargs):
        if not self.id:
            self.name_slug = pytils.translit.slugify(self.name)
        return super(Catalog, self).save(**kwargs)

    def get_absolute_url(self):
       return reverse("catalog", kwargs={"slug": self.name_slug})

    class MPTTMeta:
        order_insertion_by = ['name']
        ordering = ('sorting',)

class Journal(models.Model):
    JOURNAL_TYPE_CHOICES = (
        ('magazine', _(u'Journal')),
        ('paper', _(u'Paper')),
        ('book', _(u'Book')),
    )
    name = models.CharField(verbose_name=_('Name'),max_length=250, blank=True)
    name_slug = models.CharField(verbose_name=_('Name slug'),max_length=250, blank=True)
    description = models.TextField(verbose_name=_('Description'),max_length=250, blank=True)
    journal_type = models.CharField(verbose_name=_(u'type of journal (magazine, paper or book)'),
                                    choices=JOURNAL_TYPE_CHOICES,
                                    default='magazine',
                                    max_length=10)
    price = models.DecimalField( verbose_name=_('Price RUB'), max_digits= 12, decimal_places= 2)
    price_dram = models.DecimalField( verbose_name=_('Price DRAM'), max_digits= 12, decimal_places= 2)
    price_usd = models.DecimalField( verbose_name=_('Price USD'), max_digits= 12, decimal_places= 2)
    cover = models.ImageField(upload_to='journal_cover', verbose_name=_('Journal cover'), blank=True)
    original_id = models.IntegerField(db_index=True, verbose_name=_('Original id'))
    last_issue_id = models.IntegerField(db_index=True, verbose_name=_('Last issue id'))
    category = models.ManyToManyField(Catalog,
                                      blank=True,
                                      verbose_name=_(u'Catalogs'))
    seo_content = models.TextField(verbose_name=_(u'МЕТА content'), blank=True)
    seo_title =   models.TextField(verbose_name=_(u'МЕТА title'), blank=True)
    seo_keywords = models.TextField(verbose_name=_(u'МЕТА keywords'), blank=True)
    in_am = models.BooleanField(verbose_name=_(u'Армянские'), default=False)
    in_everyday = models.BooleanField(verbose_name=_(u'Ежедневные издания'), default=False)
    in_pressa = models.BooleanField(verbose_name=_(u'Журналы РФ'), default=False)
    in_popular_pressa = models.BooleanField(verbose_name=_(u'Часто просматриваемые'), default=False)
    recount = models.BooleanField(verbose_name=_(u'Не пересчитывать цены по курсу?'), default=False, help_text=u'Если отмечено то цены пересчитываться не будут.')
    count_for_pay = models.IntegerField(db_index=True, verbose_name=_('Count for pay'))
    def save(self, **kwargs):
        if not self.id:
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

    @property
    def get_last_issue(self):
        return Issue.objects.filter(journal=self).all().order_by('-original_id')[0:1]

    def __unicode__(self):
        return self.name
        
    def set_archive(self):
        #from catalog.models import Issue
        Issue.objects.filter(journal=self).update(is_archive=True)
        if self.count_for_pay ==0:
            payment = Issue.objects.filter(journal=self).order_by('-original_id')
        else:    
            payment = Issue.objects.filter(journal=self).order_by('-original_id')[:self.count_for_pay]    
        for p in payment:
            p.is_archive = False
            p.save()
        

class Issue(models.Model):
    journal =  models.ForeignKey(Journal, verbose_name=_('Journal'))
    cover = models.ImageField(upload_to='issue_cover', verbose_name=_('Issue cover'), blank=True)
    name = models.CharField(verbose_name=_('Name'),max_length=250, blank=True)
    date = models.DateTimeField(blank=True, null=True)
    original_id = models.IntegerField(db_index=True, verbose_name=_('Original id'))
    is_empty = models.BooleanField(verbose_name=_('Without cover'), default=True)
    is_archive = models.BooleanField(verbose_name=_('Without cover'), default=False)
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
    
    
class CurrencyHistory(models.Model):
    rub2dram = models.DecimalField( verbose_name=_('RUB to DRAM'), max_digits= 8, decimal_places= 4)
    dram2usd = models.DecimalField( verbose_name=_('DRAM to USD'), max_digits= 8, decimal_places= 4)
    date = models.DateField(blank=True, null=True)
    



def register(sender, user, request, **kwarg):   
    print 'ddddddddddddddddddddddddddddddddddddd'
    #import pdb; pdb.set_trace() 
    reg.delay(user)  
    
user_activated.connect(register)

    
            
    
    
