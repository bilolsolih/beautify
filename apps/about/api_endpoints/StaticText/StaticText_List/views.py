from rest_framework.generics import ListAPIView

from apps.about.models import StaticText
from .serializers import StaticTextListSerializer


class StaticTextListAPIView(ListAPIView):
    queryset = StaticText.objects.all()
    serializer_class = StaticTextListSerializer


__all__ = ['StaticTextListAPIView']
