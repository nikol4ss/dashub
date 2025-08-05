from django.contrib.auth.models import User

from rest_framework import viewsets

from .serializers import DatabaseConnectionSerializers


class DatabaseConnectionViewSet(viewsets.ModelViewSet):
    # Defines a CRUD ViewSet for users using the DatabaseConnectionSerializers serializer.
    queryset = User.objects.all()
    serializer_class = DatabaseConnectionSerializers
