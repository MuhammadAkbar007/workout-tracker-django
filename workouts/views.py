from django.db.models import Avg, Count, Max
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from workouts.models import Workout, WorkoutExercise
from workouts.serializers import WorkoutSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    #  filterable fields (exact matching)
    filterset_fields = ["status", "scheduled_at"]

    #  searchable fields (text search, icontains)
    search_fields = ["comment", "status"]

    # ordering fields
    ordering_fields = ["scheduled_at", "created_at", "updated_at"]
    ordering = ["-scheduled_at"]  # default ordering

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=["get"])  # type: ignore
    def report(self, request):
        user = request.user
        workouts = Workout.objects.filter(user=user)

        exercise_stats = (
            WorkoutExercise.objects.filter(workout__user=user)
            .values("exercise__name")
            .annotate(
                total_sets=Count("sets"),
                avg_reps=Avg("repetitions"),
                max_weight=Max("weight"),
            )
        )

        return Response(
            {"total_workouts": workouts.count(), "exercise_stats": list(exercise_stats)}
        )
