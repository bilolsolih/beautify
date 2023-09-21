from rest_framework.generics import RetrieveAPIView

from apps.blog.models import Post
from .serializers import PostRetrieveSerializer


class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer
    lookup_field = 'pk'


__all__ = ['PostRetrieveAPIView']
