from rest_framework.serializers import ModelSerializer


class VacancyListSerializer(ModelSerializer):
    class Meta:
        model = 'about.Vacancy'
        fields = ['id', 'title', 'location', 'vacancies']
