from rest_framework.serializers import ModelSerializer


class CollectionListSerializer(ModelSerializer):
    class Meta:
        model = 'store.Collection'
        fields = ['id', 'photo', 'title']
