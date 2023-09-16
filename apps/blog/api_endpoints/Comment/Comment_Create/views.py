from rest_framework.generics import CreateAPIView

from .serializers import CommentCreateSerializer


class CommentCreateAPIVieew(CreateAPIView):
    serializer_class = CommentCreateSerializer


__all__ = ['CommentCreateAPIVieew']
