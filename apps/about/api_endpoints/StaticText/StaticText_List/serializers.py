from rest_framework.serializers import ModelSerializer


class StaticTextListSerializer(ModelSerializer):
    class Meta:
        model = 'about.StaticText'
        fields = ['type', 'content']
