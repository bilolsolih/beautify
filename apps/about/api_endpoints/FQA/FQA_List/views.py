from django_filters.rest_framework.backends import DjangoFilterBackend
from django_filters.rest_framework.filterset import FilterSet
from rest_framework.generics import ListAPIView

from apps.about.models import FQA
from .serializers import FQAListSerializer


class FQAFilterSet(FilterSet):
    class Meta:
        model = FQA
        fields = ['type']


class FQAListAPIView(ListAPIView):
    queryset = FQA.objects.all()
    serializer_class = FQAListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FQAFilterSet


__all__ = ['FQAListAPIView']
