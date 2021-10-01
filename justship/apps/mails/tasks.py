from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import Context, Template

from .models import EmailLog

EMAIL = settings.EMAIL_HOST_USER


def render(template: str, context: dict) -> str:
    with open('justship/apps/mails/templates/mails/' + template, 'r') as file:
        text = file.read()
        tmpl = Template(text)
    return tmpl.render(Context(context))


def send_mail(sender: str, to: str, subject: str, html: str) -> None:
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


def send_system_mail(to: str, subject: str, html: str) -> None:
    """
    Send an email with from the email system
    :param to: mail to send
    :param subject: the subject of the email
    :param html: html render with email
    :return: None
    """
    send_mail(EMAIL, to, subject, html)


@shared_task
def send_recovery_mail(to: str) -> None:
    context = {'hash': 1234}
    template = render('recovery_mail.html', context)
    send_system_mail(to, 'Recuperar contraseña', template)
