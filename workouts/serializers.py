from rest_framework import serializers
from workouts.models import Workout, WorkoutExercise


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise_name = serializers.CharField(source="exercise.name", read_only=True)

    class Meta:
        model = WorkoutExercise
        fields = ["id", "exercise", "exercise_name", "repetitions", "sets", "weight"]


class WorkoutSerializer(serializers.ModelSerializer):
    workout_exercises = WorkoutExerciseSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Workout
        fields = [
            "id",
            "scheduled_at",
            "comment",
            "status",
            "created_at",
            "updated_at",
            "user",
            "workout_exercises",
        ]

    def create(self, validated_data):
        exercise_data = validated_data.pop("workout_exercises")
        workout = Workout.objects.create(**validated_data)

        for ex in exercise_data:
            WorkoutExercise.objects.create(workout=workout, **ex)

        return workout
