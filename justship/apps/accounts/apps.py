from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'justship.apps.accounts'
    label = 'accounts'
    verbose_name = 'The Accounts app'
