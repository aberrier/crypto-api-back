from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from .models import Alert
from rest_framework import viewsets
from .serializers import UserSerializer, AlertSerializer


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


class AlertViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows alerts to be viewed or edited.
    """
    queryset = Alert.objects.all().order_by('-created')
    serializer_class = AlertSerializer
