from django.apps import AppConfig


class TConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 't'

    def ready(self):
        import t.signals