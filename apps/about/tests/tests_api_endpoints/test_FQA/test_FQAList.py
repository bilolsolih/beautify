from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.about.models import FQA


class FQAListTestCase(TestCase):
    def setUp(self) -> None:
        self.endpoint = reverse('about:fqa_list')
        self.api_client = APIClient()
        instances = [
            FQA(question='test question', answer='test answer', type=FQA.QuestionType.GENERAL),
            FQA(question='test question', answer='test answer', type=FQA.QuestionType.DELIVERY)
        ]
        FQA.objects.bulk_create(instances)

    def test_ok(self):
        response = self.api_client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('test question', response.content.decode('utf-8'))
