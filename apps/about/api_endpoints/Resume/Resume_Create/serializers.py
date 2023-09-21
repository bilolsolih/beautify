from rest_framework.serializers import ModelSerializer
from apps.about.models import Resume


class ResumeCreateSerializer(ModelSerializer):
    class Meta:
        model = Resume
        fields = ['full_name', 'phone_number', 'email', 'vacancy', 'resume', 'text_resume']
