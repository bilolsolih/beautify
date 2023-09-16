from rest_framework.generics import RetrieveAPIView

from apps.store.models import Product
from .serializers import ProductRetrieveSerializer


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveSerializer
    lookup_field = 'pk'


__all__ = ['ProductRetrieveAPIView']
