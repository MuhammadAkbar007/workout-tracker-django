from rest_framework import serializers
from exercises.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"

    def validate(self, data):
        if not data.get("category") and not data.get("muscle_group"):
            raise serializers.ValidationError(
                "Exercise must have either category or muscle group"
            )
        return data
