from django.db import models


class Asset(models.Model):
    value = models.CharField(max_length=200, blank=False)
