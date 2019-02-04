from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Alert


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True, allow_blank=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

        # def create(self, validated_data):
        #     password = validated_data.pop('password', None)
        #     instance = self.Meta.model(**validated_data)
        #     if password is not None:
        #         instance.set_password(password)
        #     instance.save()
        #     return instance
        #
        # def update(self, instance, validated_data):
        #     for attr, value in validated_data.items():
        #         if attr == 'password':
        #             instance.set_password(value)
        #         else:
        #             setattr(instance, attr, value)
        #     instance.save()
        #     return instance


class AlertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'
        read_only_fields = ('created', 'updated')
