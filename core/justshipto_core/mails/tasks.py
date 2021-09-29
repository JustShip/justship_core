from celery import shared_task
from django.contrib.auth import get_user_model


@shared_task
def count_profiles():
    return get_user_model().objects.all()
