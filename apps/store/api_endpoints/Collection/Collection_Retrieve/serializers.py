from rest_framework.serializers import ModelSerializer


class CollectionRetrieveSerializer(ModelSerializer):
    class Meta:
        model = 'store.Collection'
        fields = ['id', 'photo', 'title', 'description']
