from celery import shared_task
from django.template import Context, Template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from .models import EmailLog

EMAIL = settings.EMAIL_HOST_USER


def render(template, context):
    with open('core/justshipto_core/mails/templates/mails/' + template, 'r') as file:
        text = file.read()
        tmpl = Template(text)
    return tmpl.render(Context(context))


def send_mail(sender, to, subject, html):
    msg = EmailMultiAlternatives(
        subject=subject,
        from_email=sender,
        to=to,
    )
    msg.attach_alternative(html, 'text/html')
    msg.send()

    # Save log
    EmailLog.objects.create(
        sender=sender,
        to=to,
        subject=subject,
        html=html
    )
