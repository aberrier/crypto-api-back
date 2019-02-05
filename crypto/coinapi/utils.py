import os

import requests


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
    else:
        return Exception(r.content)


def get_coin_price(asset, time=None):
    url = 'https://rest.coinapi.io/v1/exchangerate/{}/USD'.format(asset)
    if time is not None:
        url = url + '?time={}'.format(time)
    headers = {'X-CoinAPI-Key': os.environ.get('COIN_API_KEY', '')}
    r = requests.get(url, headers=headers)
    if r.status_code / 100 == 2:
        price = {"price": r.json()['rate']}
        return price
    else:
        return {"error": r.content.decode('utf-8')}
