from django.dispatch import receiver

from justship.apps.core import signals
from justship.apps.mails import tasks


@receiver(signals.user_registered)
def send_register_email_confirmation(sender, user, **kwargs):
    tasks.send_temporal_code.delay(
        to=user.email,
        temporal_code=user.temporal_code
    )
