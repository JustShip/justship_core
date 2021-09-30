from django.apps import AppConfig


class MailsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'justship.apps.mails'
    label = 'mails'
    verbose_name = 'The Mails app'

    def ready(self):
        from . import receivers
