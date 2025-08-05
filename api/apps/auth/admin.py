from django.contrib import admin


class AuthAdmin(admin.ModelAdmin):
    # Configures custom display and search of the admin interface for the Auth model.
    list_display = ("id", "email", "username", "is_active", "date_joined")
    search_fields = ("email", "id")
    readonly_fields = ("date_joined", "last_login")
