from rest_framework.serializers import ModelSerializer
from apps.accounts.models import User


class UserRetrieveSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'username', 'phone_number', 'email']
