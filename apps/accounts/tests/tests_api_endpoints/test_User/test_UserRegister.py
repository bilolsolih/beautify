from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.accounts.models import User


class UserRegisterTestCase(TestCase):
    def setUp(self) -> None:
        self.endpoint = reverse('accounts:register')
        self.api_client = APIClient()
        self.defaults = {
            'full_name': 'Bilol Muhammad Solih',
            'username': 'BlackHoler',
            'phone_number': '+998912958899',
            'email': 'BilolMuhammadSolih@gmail.com',
            'password': 'Solih1234!@#$',
            'password_check': 'Solih1234!@#$'
        }

    def test_ok(self):
        response = self.api_client.post(path=self.endpoint, data=self.defaults)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username=self.defaults['username'], phone_number=self.defaults['phone_number']).exists())

    def test_unmatching_passwords(self):
        self.defaults['password_check'] = 'Solih1234'
        response = self.api_client.post(path=self.endpoint, data=self.defaults)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Passwords do not match.', response.content.decode('utf-8'))
