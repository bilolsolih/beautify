from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.store.models import Category


class CategoryListTestCase(TestCase):
    def setUp(self) -> None:
        self.endpoint = reverse('store:category_list')
        self.api_client = APIClient()
        defaults = {
            'title': 'test category',
            'description': 'test description',
            'icon': '/testdata/images/1.jpg'
        }
        Category.objects.create(**defaults)

    def test_ok(self):
        response = self.api_client.get(path=self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('test category', response.content.decode('utf-8'))
