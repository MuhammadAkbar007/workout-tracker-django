from django.db import models


class CategoryChoice(models.TextChoices):
    CARDIO = "CARDIO", "Cardio"
    STRENGTH = "STRENGTH", "Strength"
    FLEXIBILITY = "FLEXIBILITY", "Flexibility"
    OTHER = "OTHER", "Other"


class MuscleGroupChoice(models.TextChoices):
    CHEST = "CHEST", "Chest"
    SHOULDERS = "SHOULDERS", "Shoulders"
    BACK = "BACK", "Back"
    ARMS = "ARMS", "Arms"
    LEGS = "LEGS", "Legs"
    CORE = "CORE", "Core"
    OTHER = "OTHER", "Other"


class Exercise(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    #  TODO: write validation to take category or muscle_group
    category = models.CharField(
        max_length=50,
        choices=CategoryChoice.choices,
        default=CategoryChoice.STRENGTH,
    )
    muscle_group = models.CharField(
        max_length=33,
        choices=MuscleGroupChoice.choices,
        default=MuscleGroupChoice.CHEST,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
