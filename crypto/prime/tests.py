from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, force_authenticate

from coinapi.models import Asset
from .factories import UserFactory
from .viewsets import AlertViewSet

factory = APIRequestFactory()
user = UserFactory()
fake_token = 'abc'
asset = 'BTC'
data = {"crypto": asset, "value": 10, "time_range": "2019-02-02T10:47:44Z", "type": "below"}


class TestAlertView(TestCase):
    def setUp(self):
        Asset.objects.create(value=asset)
        self.user = User.objects.create_user(username='test', email='test@test.fr')
        self.token = str(Token.objects.filter(user=self.user).get())
        self.kwargs = {'user': self.user, 'token': self.token}

    def test_get_ok(self):
        request = factory.get(reverse('prime:alerts:alert-list'))
        force_authenticate(request, **self.kwargs)
        view = AlertViewSet.as_view({'get': 'list'})
        r = view(request)
        self.assertEqual(r.status_code, 200)

    def test_not_auth(self):
        r = self.client.get(reverse('prime:alerts:alert-list'))
        self.assertEqual(r.status_code, 401)

    def test_post_ok(self):
        pass

    def test_time_range_does_not_exist_if_type_is_increase_or_decrease(self):
        pass

    def test_time_range_is_in_the_future(self):
        pass

    def test_crypto_is_not_a_valid_asset(self):
        pass

    def test_value_is_negative(self):
        pass

    def test_user_exists(self):
        pass

