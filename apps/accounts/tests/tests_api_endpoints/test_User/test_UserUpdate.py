from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.accounts.models import User


class UserUpdateTestCase(TestCase):
    def setUp(self) -> None:
        self.endpoint = reverse('accounts:update')
        self.api_client = APIClient()
        defaults = {
            'full_name': 'Bilol Muhammad Solih',
            'username': 'BlackHoler',
            'phone_number': '+998912958899',
            'email': 'BilolMuhammadSolih@gmail.com',
            'password': 'Solih1234!@#$',
        }
        self.user = User.objects.create_user(**defaults)

    def test_update_ok(self):
        self.api_client.force_login(user=self.user)
        defaults = {
            'full_name': 'Bilol Solih',
            'phone_number': '+998912968899',
            'email': 'BilolSolih@gmail.com',
        }
        response = self.api_client.patch(path=self.endpoint, data=defaults)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.filter(username='BlackHoler', **defaults).first()
        self.assertIsNotNone(user)

    def test_update_not_authenticated(self):
        defaults = {
            'full_name': 'Bilol Solih',
        }
        response = self.api_client.patch(path=self.endpoint, data=defaults)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
