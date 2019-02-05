from celery import shared_task
from .utils import send_alert_to_email
from .models import Alert, Alert_Type
from coinapi.utils import get_coin_price


@shared_task(name="alerts.send_emails")
def send_emails():
    alerts = Alert.objects.all()

    # Get the assets involved in alerts
    assets = [data.crypto for data in alerts]

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
            # Compare current price with alert price
            if alert.type == Alert_Type.BELOW and current_price < alert.value:
                message = 'The cryptocurrency {} is under {}$ with a value of {}$ right now.'.format(asset, alert.value, current_price)
                send_alert_to_email(subject, message, alert.user.email)
            if alert.type == Alert_Type.ABOVE and current_price > alert.value:
                message = 'The cryptocurrency {} is above {}$ with a value of {}$ right now.'.format(asset, alert.value, current_price)
                send_alert_to_email(subject, message, alert.user.email)
            if alert.type == Alert_Type.DECREASE or alert.type == Alert_Type.INCREASE:
                pass
    print('Started')
    send_alert_to_email()
    print('Done')
    return True
