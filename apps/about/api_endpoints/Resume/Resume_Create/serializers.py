from rest_framework.serializers import ModelSerializer


class ResumeCreateSerializer(ModelSerializer):
    class Meta:
        model = 'about.Resume'
        fields = ['full_name', 'phone_number', 'email', 'vacancy', 'resume', 'text_resume']
