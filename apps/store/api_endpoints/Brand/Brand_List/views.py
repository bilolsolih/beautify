from rest_framework.generics import ListAPIView

from apps.store.models import Brand
from .serializers import BrandListSerializer


class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer


__all__ = ['BrandListAPIView']
