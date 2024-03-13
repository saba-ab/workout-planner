from django.core.management import call_command
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.db.utils import OperationalError


@receiver(post_migrate)
def load_initial_exercise_data(sender, **kwargs):
    from .models import Exercise
    try:
        if not Exercise.objects.exists():
            call_command('loaddata', 'exercises.json')
    except OperationalError:
        pass
