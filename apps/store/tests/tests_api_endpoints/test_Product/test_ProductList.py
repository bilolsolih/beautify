from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.store.models import Brand, Category, Collection, Product, SkinType, Photo, Video


class ProductListTestCase(TestCase):
    def setUp(self) -> None:
        self.endpoint = reverse('store:product_list')
        self.api_client = APIClient()
        title = 'test title'
        description = 'test description'
        img = 'testdata/images/1.jpg'
        video = 'testdata/videos/1.mp4'
        brand = Brand.objects.create(title=title, description=description, logo=img)
        category = Category.objects.create(title=title, description=description, icon=img)
        collection = Collection.objects.create(title=title, description=description, photo=img)
        skin_type = SkinType.objects.create(title=title)
        product = Product.objects.create(
            vendor_code='123', brand=brand, category=category, title=title, description=description,
            application='test application', ingredients='test ingredients', price=123, discount=5,
        )
        product.collections.add(collection)
        product.skin_types.add(skin_type)
        Photo.objects.create(product=product, photo=img, ordinal_number=1)
        Video.objects.create(product=product, video=video, ordinal_number=1)

    def test_ok_no_filters(self):
        response = self.api_client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('test title', response.content.decode('utf-8'))

    def test_ok_filter_title(self):
        endpoint = self.endpoint + '?title=test title'
        response = self.api_client.get(endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('test title', response.content.decode('utf-8'))

    def test_wrong_filter_title(self):
        endpoint = self.endpoint + '?title=wrong title'
        response = self.api_client.get(endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotIn('test title', response.content.decode('utf-8'))

    def test_ok_filter_category(self):
        endpoint = self.endpoint + '?category=1'
        response = self.api_client.get(endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('test title', response.content.decode('utf-8'))

    def test_wrong_filter_category(self):
        endpoint = self.endpoint + '?category=2'
        response = self.api_client.get(endpoint)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Select a valid choice. That choice is not one of the available choices.', response.content.decode('utf-8'))
