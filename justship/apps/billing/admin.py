from django.contrib import admin

from . import models

@admin.register(models.BillingConfig)
class BillingConfigAdmin(admin.ModelAdmin):
    list_field = ('price_monthly', 'price_yearly')


@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_field = ('user', 'number', 'amount', 'currency', 'state')
