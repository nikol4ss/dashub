from rest_framework import serializers


def not_string(value, error_msg):
    if any(char.isdigit() for char in value):
        raise serializers.ValidationError(error_msg)
