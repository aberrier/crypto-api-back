from django.contrib.auth.models import User
from drf_enum_field.serializers import EnumFieldSerializerMixin
from rest_framework import serializers

from .models import Alert, Alert_Type


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True, allow_blank=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class AlertSerializer(EnumFieldSerializerMixin, serializers.ModelSerializer):
    def validate(self, data):
        if data['type'] in [Alert_Type.INCREASE, Alert_Type.DECREASE] and data.get('time_range') is None:
            raise serializers.ValidationError("time_range can't be null with this specific type")
        return data

    class Meta:
        model = Alert
        fields = ('id', 'crypto', 'value', 'time_range', 'type', 'user', 'last_sent')
        read_only_fields = ('created', 'updated', 'user')
