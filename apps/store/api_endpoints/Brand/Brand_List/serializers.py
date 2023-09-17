from rest_framework.serializers import ModelSerializer

from apps.store.models import Brand


class BrandListSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'title', 'logo', 'description', 'is_new', 'is_popular']
