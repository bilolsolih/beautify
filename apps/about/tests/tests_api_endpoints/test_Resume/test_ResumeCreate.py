from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.about.models import Vacancy, Resume


class ResumeCreateTestCase(TestCase):
    def setUp(self) -> None:
        self.api_client = APIClient()
        self.endpoint = reverse('about:resume_create')
        Vacancy.objects.create(title='test vacancy', location='test location', vacancies=3)

    def test_ok(self):
        with open('/mnt/WorkPlace/WebDevelopment/Projects/BackEnd/beautyweb/media/testdata/docs/1.docx', 'rb') as file:
            test_file = SimpleUploadedFile('1.docx', file.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')

        response = self.api_client.post(path=self.endpoint, data={
            'full_name': 'test full name',
            'phone_number': '+998900000000',
            'email': 'test@email.com',
            'vacancy': 1,
            'resume': test_file,
            'text_resume': 'test text resume'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Resume.objects.filter(pk=1).exists())
