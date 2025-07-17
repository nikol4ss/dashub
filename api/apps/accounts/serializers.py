from django.contrib.auth.models import User
from rest_framework import serializers

from utils.validator import not_string


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]

    def validate_first_name(self, value):
        not_string(value, "Primeiro nome inválido: não pode conter números")
        return value

    def create(self, validated_data):
        user = User(
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
            username=validated_data["username"],
            email=validated_data.get("email"),
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
