from rest_framework.serializers import ModelSerializer


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = 'blog.Comment'
        fields = ['post', 'full_name', 'email', 'comment']
