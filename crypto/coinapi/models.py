from django.db import models


class Asset(models.Model):
    """
    Model for storing all the assets of cryptocurrencies.
    Used to check the existence of a cryptocurrency.
    """
    value = models.CharField(max_length=200, blank=False)
