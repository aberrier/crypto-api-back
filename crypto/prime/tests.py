from django.test import TestCase
from .models import Alert


class AlertTestCase(TestCase):
    def setUp(self):
        Alert.objects.create(name="lion", sound="roar")
        Alert.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Alert.objects.get(name="lion")
        cat = Alert.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
