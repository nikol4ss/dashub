import re
import ipaddress

from rest_framework import serializers

from .models import DatabaseConnection


class DatabaseConnectionSerializers(serializers.ModelSerializer):
    # Serializer for the DatabaseConnection model defining the allowed fields
    class Meta:
        model = DatabaseConnection
        fields = [
            "user",
            "name",
            "database",
            "dialect",
            "username",
            "password",
            "host",
            "port",
        ]

        extra_kwargs = {"user": {"read_only": True}}

    def validate_name(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("Invalid workspace: must be a string")
        if not re.match(r"^[A-Za-z0-9\s\-]+$", value):
            raise serializers.ValidationError(
                "Invalid workspace: contains invalid characters (only letters, numbers, spaces and '-')"
            )
        return value

    def validate_database(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("Invalid database: must be a string")
        if not re.match(r"^[A-Za-z0-9\s]+$", value):
                return "Invalid database: contains invalid characters (only letters, numbers and spaces)9"
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "Invalid password: must contain at least 8 characters."
            )
        return value

    def validate_host(self, value):
        try:
            ipaddress.ip_address(value)
        except ValueError:
            raise serializers.ValidationError("Invalid host: we expect IPv4 model")
        return value

    def validate_port(self, value):
        if not isinstance(value, int) or not (1 <= value <= 65535):
            raise serializers.ValidationError(
                "Invalid port: not in the range of allowed options"
            )
        return value
