from django.db import models

from justship.apps.core.models import SingletonModel


class BillingConfig(SingletonModel):
    price_monthly = models.FloatField()
    price_yearly = models.FloatField()
    currency = models.CharField(max_length=3, default='USD')

    def __str__(self):
        return 'Billing config'
