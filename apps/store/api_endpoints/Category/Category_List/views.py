from rest_framework.generics import ListAPIView

from apps.store.models import Category
from .serializers import CategoryListSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


__all__ = ['CategoryListAPIView']
