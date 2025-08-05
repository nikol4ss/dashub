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
