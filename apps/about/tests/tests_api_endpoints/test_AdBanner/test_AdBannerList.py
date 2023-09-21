from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from apps.about.models import AdBanner


class AdBannerListTestCase(TestCase):
    def setUp(self) -> None:
        self.endpoint = reverse('about:ad_banner_list')
        self.api_client = APIClient()
        AdBanner.objects.create(title='test ad banner', photo='/testdata/images/1.jpg', link='http://127.0.0.1:8000/doc')

    def test_ok(self):
        response = self.api_client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(AdBanner.objects.filter(title='test ad banner').exists())
