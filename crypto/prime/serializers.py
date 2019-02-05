from django.contrib.auth.models import User
from drf_enum_field.serializers import EnumFieldSerializerMixin
from rest_framework import serializers

from .models import Alert, Alert_Type
from coinapi.models import Asset


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True, allow_blank=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class AlertSerializer(EnumFieldSerializerMixin, serializers.ModelSerializer):
    @staticmethod
    # Method for checking if an asset exist or not.
    def check_asset(asset):
        return bool(Asset.objects.filter(value=asset).count())

    def validate(self, data):
        # Check if time_range is provided when type increase or decrease is selected.
        if data['type'] in [Alert_Type.INCREASE, Alert_Type.DECREASE] and data.get('time_range') is None:
            raise serializers.ValidationError("time_range can't be null with this specific type")
        # Check if asset exist
        if not self.check_asset(data['crypto']):
            raise serializers.ValidationError('Invalid cryptocurrency. If you think this is an error, please try again later.')
        return data

    class Meta:
        model = Alert
        fields = ('id', 'crypto', 'value', 'time_range', 'type', 'user', 'last_sent')
        read_only_fields = ('created', 'updated', 'user')
