# -*- coding: utf-8 -*-
from django.conf import settings

DEBUG = True

# const params
PAY_SYSTEM_WM_CHECK = getattr(settings, 'PAYMASTER_PAY_SYSTEM_WM_CHECK', 02)
PAY_SYSTEM_WM_TEST = getattr(settings, 'PAYMASTER_PAY_SYSTEM_WM_TEST', 03)
PAY_SYSTEM_ALPHA_BANK = getattr(settings, 'PAYMASTER_PAY_SYSTEM_ALPHA_BANK', 8)
PAY_SYSTEM_RUS_STANDART = getattr(settings, 'PAYMASTER_PAY_SYSTEM_RUS_STANDART', 24)
PAY_SYSTEM_YANDEX = getattr(settings, 'PAYMASTER_PAY_SYSTEM_YANDEX', 30)
PAY_SYSTEM_WM = getattr(settings, 'PAYMASTER_PAY_SYSTEM_WM', 31)
PAY_SYSTEM_WM_CARD = getattr(settings, 'PAYMASTER_PAY_SYSTEM_WM_CARD', 34)
PAY_SYSTEM_BEELINE = getattr(settings, 'PAYMASTER_PAY_SYSTEM_BEELINE', 122)
PAY_SYSTEM_MTS = getattr(settings, 'PAYMASTER_PAY_SYSTEM_MTS', 102)
PAY_SYSTEM_EURONET = getattr(settings, 'PAYMASTER_PAY_SYSTEM_EURONET', 62)
PAY_SYSTEM_PROM_SVAZ = getattr(settings, 'PAYMASTER_PAY_SYSTEM_PROM_SVAZ', 64)
PAY_SYSTEM_SVAZNOY = getattr(settings, 'PAYMASTER_PAY_SYSTEM_SVAZNOY', 65)


# filled params
LMI_MERCHANT_ID = getattr(settings, 'PAYMASTER_LMI_MERCHANT_ID', '')
INVOICE_URL = getattr(settings, 'PAYMASTER_INVOICE_URL', '')
NOTIFY_URL = getattr(settings, 'PAYMASTER_NOTIFY_URL', '')
SUCCESS_URL = getattr(settings, 'PAYMASTER_SUCCESS_URL', '')
FAIL_URL = getattr(settings, 'PAYMASTER_FAIL_URL', '')
SECRET_WORD = getattr(settings, 'PAYMASTER_SECRET_WORD', '')
