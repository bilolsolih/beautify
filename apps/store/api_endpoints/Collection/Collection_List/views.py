from rest_framework.generics import ListAPIView

from apps.store.models import Collection
from .serializers import CollectionListSerializer


class CollectionListAPIView(ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionListSerializer


__all__ = ['CollectionListAPIView']
