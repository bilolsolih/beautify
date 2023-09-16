from rest_framework.serializers import ModelSerializer

from apps.accounts.models import User


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'email']
