from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

from apps.accounts.views import Signup, CentralView
from apps.accounts.urls import router

schema_view = get_schema_view(
   openapi.Info(
      title="Dashub API",
      default_version='v1',
      description="API documentation for Dashub",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # API -> Core
    path("", include(router.urls)),

    # API -> Auth (JWT)
    path("api/signup/", Signup.as_view(), name="signup"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    # API -> Browsable login (DRF)
    path("api", include("rest_framework.urls", namespace="rest_framework")),

    # API -> Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # API -> Apps
    path("api/central/", CentralView.as_view(), name="Central"),
]

# Static files & Catch-all route (SPA)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

urlpatterns += [
    re_path(r"^.*$", TemplateView.as_view(template_name="index.html")),
]
