from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.accounts.models import User


class UserDeleteTestCase(TestCase):
    def setUp(self) -> None:
        self.api_client = APIClient()
        self.endpoint = reverse('accounts:delete')
        defaults = {
            'full_name': 'Bilol Muhammad Solih',
            'username': 'BlackHoler',
            'phone_number': '+998912958899',
            'email': 'BilolMuhammadSolih@gmail.com',
            'password': 'Solih1234!@#$',
        }
        self.user = User.objects.create_user(**defaults)

    def test_ok(self):
        self.api_client.force_login(user=self.user)
        response = self.api_client.delete(path=self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        user = User.objects.get(username='BlackHoler', phone_number='+998912958899')
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_verified)

    def test_not_authenticated(self):
        response = self.api_client.delete(path=self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
