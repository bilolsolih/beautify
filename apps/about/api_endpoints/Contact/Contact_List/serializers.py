from rest_framework.serializers import ModelSerializer


class ContactListSerializer(ModelSerializer):
    class Meta:
        model = 'about.Contact'
        fields = ['full_name', 'email', 'phone_number']
