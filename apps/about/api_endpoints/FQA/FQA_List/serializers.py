from rest_framework.serializers import ModelSerializer
from apps.about.models import FQA


class FQAListSerializer(ModelSerializer):
    class Meta:
        model = FQA
        fields = ['type', 'question', 'answer']
