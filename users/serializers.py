from rest_framework import serializers
from .models import User


class LoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)
    password = serializers.CharField(max_length=256, write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "is_superuser",
        ]

        read_only_fields = ["id", "is_superuser"]
