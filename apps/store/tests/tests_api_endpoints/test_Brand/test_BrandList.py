from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.store.models import Brand


class BrandListTestCase(TestCase):
    def setUp(self) -> None:
        self.endpoint = reverse('store:brand_list')
        self.api_client = APIClient()
        defaults = {
            'title': 'test brand',
            'description': 'test description',
            'logo': '/testdata/images/1.jpg'
        }
        Brand.objects.create(**defaults)

    def test_ok(self):
        response = self.api_client.get(path=self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('test brand', response.content.decode('utf-8'))
