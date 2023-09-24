from rest_framework.serializers import ModelSerializer

from apps.store.models import Brand, Photo, Video, Product


class BrandInProduct(ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'title', 'logo']


class PhotoInProduct(ModelSerializer):
    class Meta:
        model = Photo
        fields = ['photo', 'ordinal_number']


class VideoInProduct(ModelSerializer):
    class Meta:
        model = Video
        fields = ['video', 'ordinal_number']


class ProductListSerializer(ModelSerializer):
    brand = BrandInProduct(many=False)
    photos = PhotoInProduct(many=True)
    videos = VideoInProduct(many=True)

    class Meta:
        model = Product
        fields = ['id', 'brand', 'title', 'photos', 'videos', 'price', 'discount', 'rating', 'is_new', 'is_hit', 'is_available']
