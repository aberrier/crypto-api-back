import os

from django.core.mail import send_mail


def send_alert_to_email(subject, message, receiver):
    """
    Send a mail to a specific email
    :param subject: str
    :param message: str
    :param receiver: str|email
    """
    send_mail(
        subject,
        message,
        os.environ.get('EMAIL_HOST_USER', 'test@test.com'),
        [receiver],
        fail_silently=False,
    )
    pass


def form_cleaner(querydict):
    """
    Hacky way to transform form data into readable data by the model constructor
    :param querydict: QueryDict
    :return: dict
    """
    r = dict(querydict.copy())
    # Delete the CRSF Token
    del r['csrfmiddlewaretoken']
    for key in list(r):
        # Take first element of array
        r[key] = r[key][0]
        # Delete empty fields
        if r[key] == '' or r[key] is None:
            del r[key]
    return r
