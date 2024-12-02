from django.apps import AppConfig


class CoreappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'coreapp'

    def ready(self):
        print("App is ready and signals are loaded")
        import coreapp.signals  # Import the signal receiver module
