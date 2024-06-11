from django.apps import AppConfig


class TurboappUsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "turboapp_users"
    verbose_name = "User Management turboapp users"
    alias: str = "users"
