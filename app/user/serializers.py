from djoser.serializers import UserCreateSerializer as UserCreationSerializer
from rest_framework import serializers

from rental.serializers import CarSerializer
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta(UserCreationSerializer.Meta):
        model = User
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    """List of Users"""

    class Meta:
        model = User
        fields = ['id', 'email']


class UserDetailSerializer(serializers.ModelSerializer):
    """User detail information"""

    cars = CarSerializer(many=True)

    class Meta:
        model = User
        exclude = ['password']
