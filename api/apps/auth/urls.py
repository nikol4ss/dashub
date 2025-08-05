from rest_framework import routers

from apps.auth.viewsets import AuthViewSet

# Registers the AuthViewSet on the /auth/ route using DRF's default router to automatically generate CRUD endpoints.
router = routers.DefaultRouter()
router.register(r"auth", AuthViewSet)
