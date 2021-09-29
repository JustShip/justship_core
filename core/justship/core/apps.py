from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.justship.core'
    label = 'core'
    verbose_name = 'The Core app'
