from rest_framework.generics import ListAPIView

from apps.about.models import AdBanner
from .serializers import AdBannerListSerializer


class AdBannerListAPIView(ListAPIView):
    serializer_class = AdBannerListSerializer
    queryset = AdBanner.objects.all()


__all__ = ['AdBannerListAPIView']
