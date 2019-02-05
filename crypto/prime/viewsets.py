from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from coinapi.models import Asset
from prime.models import Alert
from prime.serializers import UserSerializer, AlertSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    # Override create and update methods to fix invalid hash for password
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**request.data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        for attr, value in request.data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return Response(self.get_serializer(instance).data)


class AlertViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows alerts to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = AlertSerializer

    @staticmethod
    # Method for checking if an asset exist or not.
    def check_asset(asset):
        return bool(Asset.objects.filter(value=asset).count())

    def get_queryset(self):
        return Alert.objects.filter(user=self.request.user).order_by('-created')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Check if asset exist
        if not self.check_asset(request.data['crypto']):
            return JsonResponse({"error": 'Invalid cryptocurrency.'}, status=status.HTTP_400_BAD_REQUEST)
        instance = Alert(**request.data)
        instance.user = request.user
        instance.save()
        serializer = self.get_serializer(instance)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        for attr, value in request.data.items():
            # Check if asset exist
            if attr == 'crypto' and not self.check_asset(value):
                return JsonResponse({"error": 'Invalid cryptocurrency.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                setattr(instance, attr, value)
        instance.save()
        return Response(self.get_serializer(instance).data)