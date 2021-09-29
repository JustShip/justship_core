from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'justship.apps.api'
    label = 'api'
    verbose_name = 'The API app'
