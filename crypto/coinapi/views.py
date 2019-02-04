import os

import requests
from rest_framework.decorators import api_view
from django.http import JsonResponse


@api_view(['GET'])
def view_coin_price(request, asset, time=None):
    # TODO: Add verification of assets
    return JsonResponse(get_coin_price(asset, time))


def get_coin_price(asset, time=None):
    url = 'https://rest.coinapi.io/v1/exchangerate/{}/USD'.formacdt(asset)
    if time is not None:
        url = url + '?time={}'.format(time)
    headers = {'X-CoinAPI-Key': os.environ.get('COIN_API_KEY', '')}
    r = requests.get(url, headers=headers)
    if r.status_code / 100 == 2:
        price = {"price": r.json()['rate']}
        return price
    else:
        return {"error": r.content.decode('utf-8')}
