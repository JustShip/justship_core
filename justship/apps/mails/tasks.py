from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import Context, Template

from . import constants
from .models import EmailLog

EMAIL = settings.EMAIL_HOST_USER


def render(template: str, context: dict) -> str:
    with open('justship/apps/mails/templates/mails/' + template, 'r') as file:
        text = file.read()
        tmpl = Template(text)
    return tmpl.render(Context(context))


def send_mail(sender: str, to: [list, tuple], subject: str, html: str) -> None:
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
    send_mail(EMAIL, [to], subject, html)


@shared_task
def send_temporal_code(to: str, temporal_code: str) -> None:

    send_mail(
        sender=EMAIL,
        to=[to],
        subject='Tu código de confirmación en JustShip',
        html=render(
            template='temporal_code.html',
            context={
                'temporal_code': temporal_code,
            }
        )
    )


@shared_task
def send_password_recovery_mail(to: str, temporal_code: str) -> None:
    # link = constants.PASSWORD_RESET_URL.format(domain=domain)
    template = render('password_reset.html', {'temporal_code': temporal_code})
    send_system_mail(to, '¿Olvidaste tu contraseña?', template)
