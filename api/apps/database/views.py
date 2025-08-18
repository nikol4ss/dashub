from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import DatabaseConnectionSerializers

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class DatabaseConnection(APIView):
    # Endpoint to create a new database connection associated with the authenticated user.

    @swagger_auto_schema(
        operation_description="Create a new database connection for the authenticated user",
        request_body=DatabaseConnectionSerializers,
        responses={
            201: openapi.Response(description="Connection created successfully"),
            400: openapi.Response(description="Validation errors"),
        },
    )
    def post(self, request):
        serializer = DatabaseConnectionSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
