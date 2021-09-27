from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'justshipto_core.api'
    label = 'api'
    verbose_name = 'The API app'
