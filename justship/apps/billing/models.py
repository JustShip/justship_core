import hashlib
from django.db import models
from django.conf import settings
from django.utils.timezone import now

from . import constants
from justship.apps.core.models import SingletonModel, TimeStampedModel
from justship.apps.accounts.models import User


class BillingConfig(SingletonModel):
    price_monthly = models.FloatField()
    price_yearly = models.FloatField()
    currency = models.CharField(max_length=3, default='USD')

    def __str__(self) -> str:
        return 'Billing config'


class Transaction(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    number = models.CharField(max_length=255)
    state = models.CharField(max_length=255, default='pending', choices=(
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ))

    # billing
    amount = models.FloatField(default=1)
    currency = models.CharField(max_length=3, default='USD')
    payment_method = models.CharField(max_length=20, choices=constants.PAYMENT_METHOD_CHOICES)
    days = models.IntegerField(default=30)

    # QvaPay related
    qvapay_id = models.CharField(max_length=255, null=True, blank=True)
    qvapay_url = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.number)

    def _do_insert(self, manager, using, fields, update_pk, raw):
        self.number = hashlib.sha256(
            str(str(now()) + str(self.id)).encode()
        ).hexdigest()[:10]
        return super()._do_insert(manager, using, fields, update_pk, raw)
