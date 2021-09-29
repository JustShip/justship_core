from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'justship.apps.core'
    label = 'core'
    verbose_name = 'The Core app'
