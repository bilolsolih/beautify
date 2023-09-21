from rest_framework.serializers import ModelSerializer
from apps.about.models import AdBanner


class AdBannerListSerializer(ModelSerializer):
    class Meta:
        model = AdBanner
        fields = ['title', 'photo', 'link']
