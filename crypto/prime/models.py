from django.db import models

from django.contrib.auth.models import User
from enumfields import EnumField
from enumfields import Enum  # Uses Ethan Furman's "enum34" backport


class Alert_Type(Enum):
    BELOW = 'blw'
    ABOVE = 'abv'
    INCREASE = 'inc'
    DECREASE = 'dec'


class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = EnumField(Alert_Type, max_length=20)
    value = models.IntegerField()
    crypto = models.CharField(max_length=20)
    time_range = models.IntegerField(null=True)
    # Timestamps
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
