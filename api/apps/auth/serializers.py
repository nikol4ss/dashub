import re

from django.contrib.auth.models import User
from rest_framework import serializers


class SignupSerializer(serializers.ModelSerializer):
    # Validates registration data and creates a user with an encrypted password in the database.

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]

    def validate_first_name(self, value):
        if not re.fullmatch(r"[A-Za-z]+", value):
            raise serializers.ValidationError(
                "Invalid name: only letters (A-Z) are allowed."
            )
        return value

    def validate_last_name(self, value):
        if not re.fullmatch(r"[A-Za-z]+", value):
            raise serializers.ValidationError(
                "Invalid surname: only letters (A-Z) are allowed."
            )
        return value

    def validate_username(self, value):
        if not re.search(r"\d", value):
            raise serializers.ValidationError(
                "Invalid username: must contain at least one number."
            )
        if len(value) < 8:
            raise serializers.ValidationError(
                "Invalid username: must contain at least 8 characters."
            )
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "Invalid password: must contain at least 8 characters."
            )
        if not any(c.isupper() for c in value) or not any(c.islower() for c in value):
            raise serializers.ValidationError(
                "Invalid password: must contain both uppercase and lowercase letters."
            )
        if not any(c.isdigit() for c in value):
            raise serializers.ValidationError(
                "Invalid password: must contain at least one number."
            )
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise serializers.ValidationError(
                "Invalid password: must contain at least one special character."
            )
        if " " in value:
            raise serializers.ValidationError(
                "Invalid password: cannot contain spaces."
            )
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
