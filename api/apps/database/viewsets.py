from django.contrib.auth.models import User

from rest_framework import viewsets, permissions

from .models import DatabaseConnection
from .serializers import DatabaseConnectionSerializers


class DatabaseConnectionViewSet(viewsets.ModelViewSet):
    # Defines a CRUD ViewSet for users using the DatabaseConnectionSerializers serializer.
    queryset = DatabaseConnection.objects.all()
    serializer_class = DatabaseConnectionSerializers
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
