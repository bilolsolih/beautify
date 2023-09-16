from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.accounts.models import User


class UserRetrieveTestCase(TestCase):
    def setUp(self) -> None:
        self.endpoint = reverse('accounts:retrieve')
        self.api_client = APIClient()
        defaults = {
            'full_name': 'Bilol Muhammad Solih',
            'username': 'BlackHoler',
            'phone_number': '+998912958899',
            'email': 'BilolMuhammadSolih@gmail.com',
            'password': 'Solih1234!@#$',
        }
        self.user = User.objects.create_user(**defaults)

    def test_retrieve_ok(self):
        self.client.force_login(user=self.user)
        response = self.client.get(path=self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('BilolMuhammadSolih@gmail.com', response.content.decode('utf-8'))

    def test_retrieve_not_authenticated(self):
        response = self.client.get(path=self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('Authentication credentials were not provided.', response.content.decode('utf-8'))
