import django_filters
from django_filters.rest_framework.backends import DjangoFilterBackend
from django_filters.rest_framework.filterset import FilterSet
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from apps.store.models import Product, Brand, SkinType, Collection
from .serializers import ProductListSerializer


class CustomPageNumberPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total_pages': self.page.paginator.num_pages,
            'results': data,
        }, status=status.HTTP_200_OK)


class ProductFilterSet(FilterSet):
    price = django_filters.NumericRangeFilter(field_name='price')
    collections = django_filters.ModelMultipleChoiceFilter(field_name='collections', queryset=Collection.objects.all(), to_field_name='pk')
    brands = django_filters.ModelMultipleChoiceFilter(field_name='brand', queryset=Brand.objects.all(), to_field_name='pk')
    skin_types = django_filters.ModelMultipleChoiceFilter(field_name='skin_types', queryset=SkinType.objects.all(), to_field_name='pk')

    class Meta:
        model = Product
        fields = {
            'title': 'icontains',
            'vendor_code': 'iexact',
            'category': 'iexact',
            'is_new': 'iexact',
            'is_hit': 'iexact',
            'is_available': 'iexact',
        }
        ordering_fields = ['price', 'title', 'popularity']


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilterSet


__all__ = ['ProductListAPIView']
