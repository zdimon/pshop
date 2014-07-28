from django.db import models
from django.utils.translation import ugettext_lazy as _

class Catalog(models.Model):
    pub = models.BooleanField(verbose_name=_('Is published?'), default=False)
    name = models.CharField(verbose_name=_('Name'),max_length=250, blank=True)
    def __unicode__(self):
        return self.name