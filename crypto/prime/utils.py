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
    pass


# Hacky way to transform form data into readable data by the model constructor
def form_cleaner(querydict):
    r = dict(querydict.copy())
    del r['csrfmiddlewaretoken']
    for key in list(r):
        r[key] = r[key][0]
        if r[key] == '':
            del r[key]
    return r
