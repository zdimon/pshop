from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from catalog.models import Issue
from decimal import Decimal

class Liqpay(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, auto_now=True, blank=True, null=True)
    user = models.ForeignKey(User)
    amount = models.DecimalField(max_digits=20,decimal_places=2,default=Decimal('0.00'))
    issue =  models.ForeignKey(Issue)
    transaction_id = models.CharField(max_length=250, blank=True)
    is_success = models.BooleanField(default=False)