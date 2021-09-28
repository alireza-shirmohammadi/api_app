from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError

from .models import UserProfile


class User_profileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'