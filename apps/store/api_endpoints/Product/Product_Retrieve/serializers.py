from rest_framework.serializers import ModelSerializer
from apps.store.models import Product


class ProductRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'vendor_code', 'brand', 'category', 'title', 'description', 'application', 'ingredients', 'skin_types',
            'price', 'discount', 'rating', 'is_new', 'is_hit', 'is_available', 'created', 'photos', 'videos'
        ]
