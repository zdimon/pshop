# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User



class Payment(models.Model):
    # statuses
    STATUS_CREATED = 0
    STATUS_SELECTED = 1
    STATUS_PAYED = 2
    STATUS_ERROR = 3
    STATUS_CHOICES = (
        (STATUS_CREATED, _(u'Создан')),
        (STATUS_SELECTED, _(u'Платежная система выбрана')),
        (STATUS_PAYED, _(u'Успешно оплачен')),
        (STATUS_ERROR, _(u'Ошибка оплаты')),
    )

    payment_num = models.BigIntegerField(
        verbose_name=u'идентификатор заказа',  # номер транзакции
        default=0,
    )

    datetime = models.DateTimeField(
        verbose_name=u'дата операции',
        auto_now_add=True,
    )
    datetime_last_update = models.DateTimeField(
        verbose_name=u'дата последнего обновления',
        auto_now=True,
    )
    owner = models.ForeignKey(User,
                              verbose_name=_(u'пользователь'),
                              related_name='paymaster_payment_owner')
    operation_amount = models.DecimalField( verbose_name=_('Заявленная сумма операции'), max_digits= 12, decimal_places= 2)
    description = models.CharField(
        verbose_name=_(u'описание товара'),
        max_length=200,
        blank=True, null=True
    )
    operation_status = models.IntegerField(
        verbose_name=_(u'статус операции'),
        default=STATUS_CREATED,
        choices=STATUS_CHOICES
    )
    ammount = models.DecimalField( verbose_name=_('Ammount'), max_digits= 12, decimal_places= 2)
    system_payment_id = models.PositiveIntegerField(  # Поле получает значение в случае успешной операции
        verbose_name=_(u'номер платежа в системе PayMaster'),
        blank=True, null=True)
    payer_identifier = models.CharField(  # Поле получает значение в случае успешной операции
        verbose_name=_(u'реквизиты плательщика'), max_length=100, default=' ')

    def is_finished(self):
        return self.system_payment_id is not None
