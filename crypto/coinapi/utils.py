from ..prime.models import Alert
import requests
import os


def send_mail(alert):
    pass


def get_list_assets():
    headers = {'X-CoinAPI-Key': os.environ.get('COIN_API_KEY', '')}
    r = requests.get('https://rest.coinapi.io/v1/assets', headers=headers)
    if r.status_code / 100 == 2:
        assets = []
        for asset in r.json():
            if asset['type_is_crypto']:
                assets.append(asset['asset_id'])
        return assets
