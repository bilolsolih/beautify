from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from apps.about.models import Contact


class ContactListTestCase(TestCase):
    def setUp(self) -> None:
        self.endpoint = reverse('about:contact_list')
        self.api_client = APIClient()
        Contact.objects.create(full_name='test contact', email='test@email.com', phone_number='+998900000000')

    def test_ok(self):
        response = self.api_client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('test contact', response.content.decode('utf-8'))
