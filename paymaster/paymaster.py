# -*- coding: utf-8 -*-

from base64 import b64encode
from hashlib import md5
from urllib import urlencode

from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

#from accounts.models import Customer
from models import Payment
from settings import *
from catalog.models import Issue


def pay(request, issue_id, **kwargs):
    """
    Параметры:
    payment_num -- ID покупки в системе продавца (ID транзакции)
    payment_system -- одна из платежных систем из settings.py
    amount -- сумма к оплате
    description -- выводимое на paymaster описание товара
    user -- accounts.Customer -- текущий покупатель

    Возвращает:
    redirect -- на сайт paymaster

    Отсылка формы запроса платежа, одновременно перенаправляет пользователя
    на сайт paymaster

    Отсылаемые поля:
    LMI_MERCHANT_ID - settings
    LMI_PAYMENT_AMOUNT - param
    LMI_CURRENCY - 'RUB'
    LMI_PAYMENT_NO - payment_num
    LMI_PAYMENT_DESC - param
    LMI_PAYER_PHONE_NUMBER - param
    LMI_PAYER_EMAIL - param
    LMI_PAYMENT_SYSTEM - param???
    + PAYMENT_ID - ID новой записи о платеже в базе

    Пример, только из обязательных полей
    https://paymaster.ru/Payment/Init?LMI_MERCHANT_ID=R191483760831&LMI_PAYMENT_AMOUNT=1488&LMI_CURRENCY=RUB&LMI_PAYMENT_NO=123123&LMI_PAYMENT_DESC=123123
    """
    user = request.user
    issue = Issue.objects.get(pk=issue_id)
    payment = Payment.objects.create(
        owner=user,
        operation_amount=issue.journal.price,
        description='payment'
    )

    data = {
        'LMI_MERCHANT_ID': 'd7706dd6-acc2-4821-9fcf-1b58999ac2cd',
        'LMI_PAYMENT_AMOUNT': str('100'),
        'LMI_CURRENCY': 'RUB',
        'LMI_PAYMENT_NO': str('456'),
        'LMI_PAYMENT_DESC': 'payment',
        'LMI_PAYER_PHONE_NUMBER': '',
        'LMI_PAYER_EMAIL': user.email or '',
        'PAYMENT_ID': payment.pk,
    }

    #if DEBUG:
    #    data['LMI_INVOICE_CONFIRMATION_URL'] = INVOICE_URL
    #    data['LMI_PAYMENT_NOTIFICATION_URL'] = NOTIFY_URL
    #    data['LMI_SUCCESS_URL'] = SUCCESS_URL


    url = 'https://paymaster.ru/Payment/Init?' + urlencode(data)
    return redirect(url)


def invoice(request):
    """
    Пользователь собирается проводить платеж.
    Необходимо проверить данные, и отослать YES

    Проверяется:
    LMI_MERCHANT_ID
    LMI_PAYMENT_NO
    LMI_PAYMENT_AMOUNT
    LMI_PAID_AMOUNT
    LMI_PAID_CURRENCY
    LMI_PAYMENT_SYSTEM
    + PAYMENT_ID
    """
    data = [request.POST, request.GET][len(request.POST) == 0]
    pay_pk = int(data['PAYMENT_ID'])
    payment = Payment.objects.get(pk=pay_pk)

    # TODO: можно ли, если запрошено, например 60 рублей, заплатить 2 доллара?
    check = data['LMI_MERCHANT_ID'] == LMI_MERCHANT_ID and \
        float(data['LMI_PAYMENT_AMOUNT']) == payment.operation_amount and \
        data['LMI_CURRENCY'] == 'RUB' and \
        float(data['LMI_PAID_AMOUNT']) == payment.operation_amount and \
        data['LMI_PAID_CURRENCY'] == 'RUB' and \
        data['LMI_PAYMENT_DESC'] == payment.description

    if check:
        payment.operation_status = Payment.STATUS_SELECTED
        payment.save()
        return HttpResponse('YES')
    else:
        payment.operation_status = Payment.STATUS_ERROR
        payment.save()
        return HttpResponse('NO')


def calc_hash(data):
    in_str = ';'.join(
        [
            LMI_MERCHANT_ID,
            data['LMI_PAYMENT_NO'],
            data['LMI_SYS_PAYMENT_ID'],
            data['LMI_SYS_PAYMENT_DATE'],
            data['LMI_PAYMENT_AMOUNT'],
            data['LMI_CURRENCY'],
            data['LMI_PAID_AMOUNT'],
            data['LMI_PAID_CURRENCY'],
            data['LMI_PAYMENT_SYSTEM'],
            data.get('LMI_SIM_MODE', ''),
            SECRET_WORD,
        ]
    )

    return b64encode(md5(str(in_str)).digest())


@csrf_exempt
def notify(request):
    """
    Пользователь отдал деньги, необходимо предоставить ему услугу

    LMI_SYS_PAYMENT_ID -- ID платежа в PayMaster, нужно сохранить
    LMI_PAYMENT_AMOUNT
    LMI_CURRENCY
    LMI_PAID_AMOUNT
    LMI_PAID_CURRENCY
    LMI_PAYMENT_SYSTEM
    LMI_HASH
    LMI_PAYER_IDENTIFIER

    Нужные параметры прописываются к Payment с данным ID
    """
    data = [request.POST, request.GET][len(request.POST) == 0]
    pay_pk = int(data['PAYMENT_ID'])
    payment = Payment.objects.get(pk=pay_pk)

    req_hash = data['LMI_HASH']
    cal_hash = calc_hash(data)
    if req_hash == cal_hash:
        payment.operation_real_payed = float(data['LMI_PAID_AMOUNT'])
        if 'LMI_PAYER_IDENTIFIER' in data:
            payment.payer_identifier = data['LMI_PAYER_IDENTIFIER']
        payment.system_payment_id = data['LMI_SYS_PAYMENT_ID']
        payment.operation_status = Payment.STATUS_PAYED
    else:
        payment.operation_status = Payment.STATUS_ERROR

    payment.save()
    return HttpResponse('')  # ответ игнорируется системой Paymaster


def success(request):
    return HttpResponse('<h1>SUCCESS</h1>')


def fail(request):
    return HttpResponse('<h1>ERROR</h1>')
