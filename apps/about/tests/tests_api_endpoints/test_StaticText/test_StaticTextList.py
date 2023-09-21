from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from apps.about.models import StaticText


class StaticTextListTestCase(TestCase):
    def setUp(self) -> None:
        self.endpoint = reverse('about:static_text_list')
        self.api_client = APIClient()
        StaticText.objects.create(type='a', content='test content')

    def test_ok(self):
        response = self.api_client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('test content', response.content.decode('utf-8'))
