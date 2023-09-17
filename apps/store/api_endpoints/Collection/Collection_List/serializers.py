from rest_framework.serializers import ModelSerializer

from apps.store.models import Collection


class CollectionListSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'photo', 'title', 'description']
