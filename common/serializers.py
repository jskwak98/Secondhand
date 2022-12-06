from rest_framework import serializers, generics
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'broker_id', 'username')

