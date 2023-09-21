from rest_framework.serializers import ModelSerializer
from apps.about.models import Contact


class ContactListSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone_number']
