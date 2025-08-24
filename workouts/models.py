from django.conf import settings
from django.db import models
from django.utils import timezone


class Status(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    PENDING = "PENDING", "Pending"
    COMPLETED = "COMPLETED", "Completed"


class Workout(models.Model):
    scheduled_at = models.DateTimeField(default=timezone.now)
    comment = models.TextField(blank=True)
    status = models.CharField(
        max_length=33, choices=Status.choices, default=Status.PENDING
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="workouts"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-scheduled_at"]

    def __str__(self) -> str:
        return f"Workout for {self.user.email} on {self.scheduled_at.date()}: {self.status}"


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(
        Workout, on_delete=models.CASCADE, related_name="workout_exercises"
    )
    exercise = models.ForeignKey(
        "exercises.Exercise", on_delete=models.CASCADE, related_name="workout_exercises"
    )
    repetitions = models.IntegerField()
    sets = models.IntegerField()
    weight = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ("workout", "exercise")

    def __str__(self) -> str:
        return (
            f"{self.exercise.name} ({self.sets} x {self.repetitions}, {self.weight} kg)"
        )
