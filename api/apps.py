from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        from django.core.management import call_command
        from django.db.utils import OperationalError
        from .models import Exercise
        try:
            if not Exercise.objects.exists():
                call_command('loaddata', 'exercises.json')
        except OperationalError:
            # raise OperationalError(
            #     "Database table for Exercise model doesn't exist. Did you forget to migrate? Original error: {}".format(e))
            pass
