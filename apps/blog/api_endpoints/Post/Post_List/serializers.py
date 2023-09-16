from rest_framework.serializers import ModelSerializer


class PostListSerializer(ModelSerializer):
    class Meta:
        model = 'blog.Post'
        fields = ['id', 'photo', 'title', 'created']
