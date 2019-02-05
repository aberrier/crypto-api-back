import os

from django.core.mail import send_mail


def send_alert_to_email(subject, message, receiver):
    send_mail(
        subject,
        message,
        os.environ.get('EMAIL_HOST_USER', 'test@test.com'),
        [receiver],
        fail_silently=False,
    )


