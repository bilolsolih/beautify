from rest_framework.generics import RetrieveAPIView

from apps.store.models import Collection
from .serializers import CollectionRetrieveSerializer


class CollectionRetrieveAPIView(RetrieveAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionRetrieveSerializer
    lookup_field = 'pk'


__all__ = ['CollectionRetrieveAPIView']
