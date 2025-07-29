from django.contrib import admin
from django.views.generic import TemplateView
from apps.accounts.views import Signup, DashboardView

from django.conf import settings
from apps.accounts.urls import router

from django.conf.urls.static import static
from django.urls import path, re_path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/", include("rest_framework.urls", namespace="rest_framework")),

    path("api/signup/", Signup.as_view(), name="signup"),

    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("api/dashboard/", DashboardView.as_view(), name="dashboard"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

urlpatterns += [
    re_path(r"^.*$", TemplateView.as_view(template_name="index.html")),
]
