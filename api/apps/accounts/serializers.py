from django.contrib.auth.models import User
from rest_framework import serializers

import re


class UserSerializer(serializers.ModelSerializer):
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

        if not re.search(R"\d", value):
            raise serializers.ValidationError(
                "Invalid username: only letters and numbers are allowed."
            )

        elif len(value) < 8:
            raise serializers.ValidationError(
                "Invalid username: must contain at least 8 characters."
            )
        return value

    def validate_password(self, value):

        if len(value) < 8:
            raise serializers.ValidationError(
                "Invalid password: must contain at least 8 characters."
            )

        elif not any(field.isupper() for field in value) or not any(
            field.islower() for field in value
        ):
            raise serializers.ValidationError(
                "Invalid password: must contain both uppercase and lowercase letters."
            )

        elif not any(field.isdigit() for field in value):
            raise serializers.ValidationError(
                "Invalid password: must contain at least one number."
            )

        elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise serializers.ValidationError(
                "Invalid password: must contain at least one special character."
            )

        elif " " in value:
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
