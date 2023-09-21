from rest_framework.serializers import ModelSerializer
from apps.about.models import StaticText


class StaticTextListSerializer(ModelSerializer):
    class Meta:
        model = StaticText
        fields = ['type', 'content']
