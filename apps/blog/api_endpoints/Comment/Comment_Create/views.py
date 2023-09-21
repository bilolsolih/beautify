from rest_framework.generics import CreateAPIView

from .serializers import CommentCreateSerializer


class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentCreateSerializer


__all__ = ['CommentCreateAPIView']
