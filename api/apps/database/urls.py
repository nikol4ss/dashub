from apps.database.viewsets import DatabaseConnectionViewSet

from rest_framework import routers

# Registers the DatabaseConnectionViewSet on the /database/ route for automatic CRUD operations.
router = routers.DefaultRouter()
router.register(r"database", DatabaseConnectionViewSet)
