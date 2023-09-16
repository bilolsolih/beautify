from rest_framework.generics import ListAPIView

from apps.about.models import Vacancy
from .serializers import VacancyListSerializer


class VacancyListAPIView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer


__all__ = ['VacancyListAPIView']
