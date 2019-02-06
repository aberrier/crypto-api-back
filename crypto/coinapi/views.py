from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .models import Asset
from .serializers import AssetSerializer
from .utils import get_coin_price


@api_view(['GET'])
def view_coin_price(request, asset, time=None):
    """
    Endpoint for querying the CoinAPI
    :param asset: str
    :param time: datetime.datetime.isoformat
    :return: JsonResponse
    """
    return JsonResponse(get_coin_price(asset, time))


class AssetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows assets to be viewed or edited.
    """
    queryset = Asset.objects.all().order_by('value')
    serializer_class = AssetSerializer
