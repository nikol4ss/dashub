from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView

from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from apps.auth.views import Signup, CentralView
from apps.auth.urls import router
from apps.database.views import DatabaseConnection


schema_view = get_schema_view(
    openapi.Info(
        title="Dashub API",
        default_version="v1",
        description="API documentation for Dashub",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include(router.urls)),

    # JWT auth
    path("api/signup/", Signup.as_view(), name="signup"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Password reset
    path(
        "api/password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),

    # DRF browsable API login/logout
    path("api", include("rest_framework.urls", namespace="rest_framework")),

    # Swagger UI
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),

    path("api/central/", CentralView.as_view(), name="central"),
    path("api/db/connect", DatabaseConnection.as_view(), name="database_connect"),
]

# Static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

# SPA catch-all route
urlpatterns += [
    re_path(r"^.*$", TemplateView.as_view(template_name="index.html")),
]
