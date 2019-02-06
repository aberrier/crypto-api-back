from django.contrib.auth.models import User
from factory import SubFactory
from factory.django import DjangoModelFactory

from .models import Alert


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = 'bilal.hassani'
    email = 'bilal.hassani@fakemail.com'


class AlertFactory(DjangoModelFactory):
    class Meta:
        model = Alert

    user = SubFactory(UserFactory)
