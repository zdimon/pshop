# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^Webmoney/invoice/$', 'paymaster.paymaster.invoice'),
    url(r'^Webmoney/notify/$', 'paymaster.paymaster.notify'),
    url(r'^Webmoney/success/$', 'paymaster.paymaster.success'),
    url(r'^Webmoney/fail/$', 'paymaster.paymaster.fail'),
    url(r'^payment/pay/(?P<issue_id>\d+)$','paymaster.paymaster.pay', name="payment-pay"),
)