from celery import shared_task


@shared_task(name="alerts.asset_list")
def asset_list():
    print('Bob')


@shared_task(name="alerts.send_emails")
def send_emails():
    print('Eponge')
