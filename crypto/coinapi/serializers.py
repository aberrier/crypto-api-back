from rest_framework import serializers


class CoinAPISerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    crypto = serializers.CharField(max_length=20)
    time = serializers.TimeField()
