from .serializers import UserSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@method_decorator(csrf_exempt, name="dispatch")
class Signup(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Create a new user account",
        request_body=UserSerializer,
        responses={
            201: openapi.Response(description="User created successfully"),
            400: openapi.Response(description="Validation errors"),
        },
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "User created"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name="dispatch")
class CentralView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get authenticated user Central info",
        responses={
            200: openapi.Response(
                description="User authenticated",
                examples={
                    "application/json": {
                        "message": "You are authenticated",
                        "user": "username_here",
                    }
                },
            ),
            401: openapi.Response(description="Unauthorized"),
        },
    )
    def get(self, request):
        return Response({"message": "You are authenticated", "user": str(request.user)})
