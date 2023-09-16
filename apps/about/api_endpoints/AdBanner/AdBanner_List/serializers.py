from rest_framework.serializers import ModelSerializer


class AdBannerListSerializer(ModelSerializer):
    class Meta:
        model = 'about.AdBanner'
        fields = ['title', 'photo', 'link']
