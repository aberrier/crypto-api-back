from celery import shared_task

@shared_task(name="alerts.send_emails")
def send_emails():
    print('Eponge')
