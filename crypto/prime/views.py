from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.template import loader
from .models import Alert
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, AlertSerializer
from django.shortcuts import get_object_or_404

def index(request, num=None):
    template = loader.get_template('prime/index.html')
    context = {
        'num': num
    }
    return HttpResponse(template.render(context, request))


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    # Override of create and update methods to fix invalid hash for password
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
    queryset = Alert.objects.all().order_by('-created')
    serializer_class = AlertSerializer
