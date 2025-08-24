from django.apps import apps
from django.db import transaction


def seed_exercises(sender, **kwargs):
    _ = sender, kwargs  # to silence pyright complaining
    Exercise = apps.get_model("exercises", "Exercise")
    seed_data = [
        {
            "name": "Push-up",
            "description": "A bodyweight exercise for chest, shoulders, and triceps.",
            "category": "STRENGTH",
            "muscle_group": "CHEST",
        },
        {
            "name": "Squat",
            "description": "A lower body exercise targeting quadriceps, hamstrings, and glutes.",
            "category": "FLEXIBILITY",
            "muscle_group": "LEGS",
        },
        {
            "name": "Bench Press",
            "description": "A chest exercise using a barbell or dumbbells.",
            "category": "STRENGTH",
            "muscle_group": "CHEST",
        },
        {
            "name": "Deadlift",
            "description": "A compound lift working back, glutes, hamstrings, and grip.",
            "category": "STRENGTH",
            "muscle_group": "BACK",
        },
    ]

    with transaction.atomic():
        for data in seed_data:
            obj, created = Exercise.objects.get_or_create(
                name=data["name"], defaults=data
            )
            if not created:
                # update values if not created
                for field, value in data.items():
                    setattr(obj, field, value)
                obj.save()
