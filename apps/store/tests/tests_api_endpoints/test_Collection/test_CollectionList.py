from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.store.models import Collection


class CollectionListTestCase(TestCase):
    def setUp(self) -> None:
        self.endpoint = reverse('store:collection_list')
        self.api_client = APIClient()
        defaults = {
            'title': 'test collection',
            'description': 'test description',
            'photo': '/testdata/images/1.jpg'
        }
        Collection.objects.create(**defaults)

    def test_ok(self):
        response = self.api_client.get(path=self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('test collection', response.content.decode('utf-8'))
