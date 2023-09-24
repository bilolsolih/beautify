from rest_framework.serializers import ModelSerializer

from apps.store.models import Review


class ReviewCreateSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ['product', 'rating', 'review']

    def create(self, validated_data):
        product, rating, review = validated_data
        self.context['request'].user.reviewed_products.add(product, through_defaults={'rating': rating, 'review': review})
