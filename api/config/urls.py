from django.contrib import admin
from apps.accounts.views import Signup
from django.views.generic import TemplateView

from django.conf import settings
from apps.accounts.urls import router

from django.conf.urls.static import static
from django.urls import path, re_path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    # accounts
    path("api/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/signup/", Signup.as_view(), name="signup"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

urlpatterns += [
    re_path(r"^.*$", TemplateView.as_view(template_name="index.html")),
]
