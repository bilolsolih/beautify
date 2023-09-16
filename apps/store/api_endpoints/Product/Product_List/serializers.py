from rest_framework.serializers import ModelSerializer


class BrandInProduct(ModelSerializer):
    class Meta:
        model = 'store.Brand'
        fields = ['id', 'title', 'photo']


class PhotoInProduct(ModelSerializer):
    class Meta:
        model = 'store.Photo'
        fields = ['photo', 'ordinal_number']


class ProductListSerializer(ModelSerializer):
    brand = BrandInProduct(many=False)
    photos = PhotoInProduct(many=True)

    class Meta:
        model = 'store.Product'
        fields = ['id', 'brand', 'title', 'photos', 'price', 'discount', 'rating', 'is_new', 'is_hit', 'is_available']
