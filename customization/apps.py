from django.apps import AppConfig


class CustomizationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customization'
    verbose_name = 'атрибуты'
