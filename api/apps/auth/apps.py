from django.apps import AppConfig


class AuthConfig(AppConfig):
    # Configures app auth by registering its signals when starting Django.
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.auth"
    label = "custom_auth"

    def ready(self):
        import apps.auth.signals
