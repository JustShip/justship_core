from graphene_django import DjangoObjectType

from justship.apps.billing.models import Transaction, BillingConfig


class TransactionType(DjangoObjectType):
    class Meta:
        model = Transaction
        only_fields = (
            'user',
            'number',
            'state',
            'amount',
            'currency',
            'payment_method',
            'days',
            'qvapay_id',
            'qvapay_url'
        )


class BillingConfigType(DjangoObjectType):
    class Meta:
        model = BillingConfig
        only_fields = (
            'price_monthly',
            'price_yearly',
            'currency'
        )


billing_types = [
    TransactionType,
    BillingConfigType
]
