from celery import shared_task
from .models import Profile


@shared_task
def count_profiles():
    return Profile.objects.all()
