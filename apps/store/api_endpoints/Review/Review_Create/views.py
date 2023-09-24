from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import ReviewCreateSerializer


class ReviewCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewCreateSerializer


__all__ = ['ReviewCreateAPIView']
