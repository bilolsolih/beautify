from rest_framework.serializers import ModelSerializer


class FQAListSerializer(ModelSerializer):
    class Meta:
        model = 'about.FQA'
        fields = ['type', 'question', 'answer']
