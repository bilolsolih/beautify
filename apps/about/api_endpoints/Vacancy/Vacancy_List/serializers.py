from rest_framework.serializers import ModelSerializer

from apps.about.models import Vacancy


class VacancyListSerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['id', 'title', 'location', 'vacancies']
