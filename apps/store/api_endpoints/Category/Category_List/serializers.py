from rest_framework.serializers import ModelSerializer

from apps.store.models import Category


class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'icon', 'description']
