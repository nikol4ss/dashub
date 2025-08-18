from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import SignupSerializer


@method_decorator(csrf_exempt, name="dispatch")
class Signup(APIView):
    """
    Endpoint to register a new user.
    Accepts registration data and creates a new user account.
    """

    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Register a new user by providing necessary account details",
        request_body=SignupSerializer,
        responses={
            201: openapi.Response(
                description="New user account created successfully",
                schema=SignupSerializer,
            ),
            400: openapi.Response(
                description="Validation errors in the submitted data"
            ),
        },
    )
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "User created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name="dispatch")
class CentralView(APIView):
    """
    Endpoint to retrieve information about the authenticated user.
    Returns user-specific data confirming authentication status.
    """

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve authenticated user information",
        responses={
            200: openapi.Response(
                description="Authenticated user data returned successfully",
                examples={
                    "application/json": {
                        "message": "You are authenticated",
                        "user": "username_here",
                    }
                },
            ),
            401: openapi.Response(description="User is not authenticated"),
        },
    )
    def get(self, request):
        return Response(
            {
                "message": "You are authenticated",
                "user": str(request.user),
            }
        )
