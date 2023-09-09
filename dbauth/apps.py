from django.apps import AppConfig


class DbauthConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "dbauth"

def ready(self):
    import dbauth.signals