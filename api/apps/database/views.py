from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import DatabaseConnectionSerializers


class DatabaseConnection(APIView):
    # Receives database connection data via POST, validates and saves it using the serializer.
    def post(self, request):
        serializer = DatabaseConnectionSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
