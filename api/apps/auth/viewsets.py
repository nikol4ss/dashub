from django.contrib.auth.models import User

from rest_framework import viewsets

from .serializers import SignupSerializer


class AuthViewSet(viewsets.ModelViewSet):
    # Exposes user CRUD operations using the registration serializer via a DRF ViewSet.
    queryset = User.objects.all()
    serializer_class = SignupSerializer
