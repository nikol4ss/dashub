from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

from django.conf.urls.static import static
from django.urls import path, re_path

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

urlpatterns += [
    re_path(r"^.*$", TemplateView.as_view(template_name="index.html")),
]
