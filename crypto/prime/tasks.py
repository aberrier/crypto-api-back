# Celery important tasks
import os

from celery import shared_task
from .utils import send_alert_to_email
from .models import Alert, Alert_Type
from coinapi.utils import get_coin_price
from datetime import datetime, timedelta

email_cycle = int(os.environ.get('EMAIL_REFRESH_CYCLE', '24'))


@shared_task(name="alerts.send_emails")
def send_emails():
    """
    Send emails for every alert that has been activated
    """
    def _send_emails(_subject, _message):
        """
        Inner function to avoid redundancy
        :param _subject: str
        :param _message: str
        """
        nonlocal nb_emails, alert
        # Send email
        send_alert_to_email(_subject, _message, alert.user.email)
        # Update of the last_sent field
        alert.last_sent = datetime.now()
        alert.save()
        # Update counter
        nb_emails = nb_emails + 1

    alerts = Alert.objects.all()

    # Get the assets involved in alerts
    assets = [data.crypto for data in alerts]
    assets = list(set(assets))
    nb_emails = 0

    # Check the state of each asset
    for asset in assets:
        current_price = get_coin_price(asset)
        if current_price.get('price'):
            current_price = current_price['price']
        else:
            print('Error for {} : {}'.format(asset, current_price))
            continue

        # Get alerts involved with this asset
        alerts_of_asset = Alert.objects.filter(crypto=asset)
        subject = 'Crypto Alert : {}'.format(asset)
        for alert in alerts_of_asset:
            # Check if alert had already been sent
            if alert.last_sent.replace(tzinfo=None) < datetime.now() - timedelta(hours=email_cycle):
                # Compare current price with alert price
                if alert.type == Alert_Type.BELOW and current_price < alert.value:
                    message = 'The cryptocurrency {} is under {}$ with a value of {:.2f}$ right now.'.format(asset, alert.value, current_price)
                    _send_emails(subject, message)
                if alert.type == Alert_Type.ABOVE and current_price > alert.value:
                    message = 'The cryptocurrency {} is above {}$ with a value of {:.2f}$ right now.'.format(asset, alert.value, current_price)
                    _send_emails(subject, message)
                if alert.type == Alert_Type.DECREASE or alert.type == Alert_Type.INCREASE:
                    date = alert.time_range.replace(tzinfo=None)
                    # Get the price which corresponds to time_range
                    old_price = get_coin_price(asset, date.isoformat())
                    if old_price.get('price'):
                        old_price = old_price['price']
                    else:
                        print('Error for {}: {}'.format(asset, old_price))
                        continue
                    ratio = 100 - 100 * (current_price / old_price)
                    if alert.type == Alert_Type.DECREASE and ratio > alert.value:
                        message = 'The cryptocurrency {} decreased by {}% with a value of {:.2f}$ right now.'.format(asset, ratio, current_price)
                        _send_emails(subject, message)
                    if alert.type == Alert_Type.INCREASE and -ratio > alert.value:
                        message = 'The cryptocurrency {} increase by {}% with a value of {:.2f}$ right now.'.format(asset, -ratio, current_price)
                        _send_emails(subject, message)
    print('Number of emails sent : {}'.format(nb_emails))
    return True


