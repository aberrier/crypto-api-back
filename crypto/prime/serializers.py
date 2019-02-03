from django.contrib.auth.models import User
from .models import Alert
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class AlertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alert
        fields = ('id', 'user', 'type', 'value', 'crypto', 'time_range')
