from rest_framework.generics import ListAPIView

from apps.about.models import Contact
from .serializers import ContactListSerializer


class ContactListAPIView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer


__all__ = ['ContactListAPIView']
