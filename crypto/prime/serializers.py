from django.contrib.auth.models import User
from drf_enum_field.serializers import EnumFieldSerializerMixin
from rest_framework import serializers

from .models import Alert


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True, allow_blank=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class AlertSerializer(EnumFieldSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ('id', 'crypto', 'value', 'time_range', 'type', 'user')
        read_only_fields = ('created', 'updated', 'user')
