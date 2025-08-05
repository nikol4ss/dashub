from django.apps import AppConfig


class DatabaseConnectionConfig(AppConfig):
    # Configures the app database for logging to Django.
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.database"
