# Celery tasks relative to CoinAPI

from celery import shared_task
from .models import Asset
from .utils import get_list_assets


@shared_task(name="coinapi.asset_list")
def asset_list():
    """
    Update the list of assets periodically
    """
    list_stored = [data.value for data in Asset.objects.all()]
    list_new = get_list_assets()
    size_new = 0
    for new_asset in list_new:
        # Identify new coins
        if new_asset not in list_stored:
            Asset.objects.create(value=new_asset)
            size_new = size_new + 1
        # Identify coins that no longer exist.
        else:
            list_stored.pop(list_stored.index(new_asset))
    Asset.objects.filter(value__in=list_stored).delete()
    size_removed = len(list_stored)
    print('Added {} asset(s) and removed {} asset(s)'.format(size_new, size_removed))
