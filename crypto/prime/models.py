from django.db import models

from django.contrib.auth.models import User
from enumfields import EnumField
from enumfields import Enum


class Alert_Type(Enum):
    BELOW = 'below'
    ABOVE = 'above'
    INCREASE = 'increase'
    DECREASE = 'decrease'


class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = EnumField(Alert_Type, max_length=20, blank=False)
    value = models.IntegerField(blank=False)
    crypto = models.CharField(max_length=20, blank=False)
    time_range = models.IntegerField(blank=True)
    # Timestamps
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
