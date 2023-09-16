from rest_framework.generics import CreateAPIView

from .serializers import ResumeCreateSerializer


class ResumeCreateAPIView(CreateAPIView):
    serializer_class = ResumeCreateSerializer


__all__ = ['ResumeCreateAPIView']
