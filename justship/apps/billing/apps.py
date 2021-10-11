from django.apps import AppConfig


class BillingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'justship.apps.billing'
    label = 'billing'
    verbose_name = 'The Billing app'
