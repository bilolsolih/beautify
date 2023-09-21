from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.about.models import Vacancy


class VacancyListTestCase(TestCase):
    def setUp(self) -> None:
        self.endpoint = reverse('about:vacancy_list')
        self.api_client = APIClient()
        Vacancy.objects.create(title='test vacancy', location='test location', vacancies=3)

    def test_ok(self):
        response = self.api_client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('test vacancy', response.content.decode('utf-8'))
