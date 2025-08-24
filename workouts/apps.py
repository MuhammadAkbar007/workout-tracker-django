from django.apps import AppConfig
from django.db.models.signals import post_migrate

from .signals import seed_exercises


class WorkoutsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "workouts"

    def ready(self):
        post_migrate.connect(seed_exercises, sender=self)
