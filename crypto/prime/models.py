from datetime import datetime

from django.db import models

from django.contrib.auth.models import User
from enumfields import EnumField
from enumfields import Enum
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


# When a new user has been created, a associated token is also created.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Alert_Type(Enum):
    BELOW = 'below'
    ABOVE = 'above'
    INCREASE = 'increase'
    DECREASE = 'decrease'


class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = EnumField(Alert_Type, max_length=20, blank=False)
    value = models.IntegerField(blank=False)
    crypto = models.CharField(max_length=200, blank=False)
    time_range = models.DateTimeField(default=datetime.now, blank=True)
    last_sent = models.DateTimeField(default=datetime.fromtimestamp(0), blank=True)
    # Timestamps
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
