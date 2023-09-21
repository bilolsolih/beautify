from rest_framework.serializers import ModelSerializer


class CommentInPost(ModelSerializer):
    class Meta:
        model = 'blog.Comment'
        fields = ['id', 'full_name', 'comment']


class PostRetrieveSerializer(ModelSerializer):
    comments = CommentInPost(many=True)

    class Meta:
        model = 'blog.Post'
        fields = ['id', 'title', 'photo', 'content', 'comments', 'created']
