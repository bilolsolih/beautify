import django_filters
from django_filters.rest_framework.backends import DjangoFilterBackend
from django_filters.rest_framework.filterset import FilterSet
from rest_framework.generics import ListAPIView

from apps.blog.models import Post
from .serializers import PostListSerializer


class PostFilterSet(FilterSet):
    year = django_filters.DateFilter(field_name='created__year', lookup_expr='iexact')
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilterSet


__all__ = ['PostListAPIView']
