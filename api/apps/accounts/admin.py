from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "username", "is_active", "date_joined")
    search_fields = ("email", "id")
    readonly_fields = ("date_joined", "last_login")
