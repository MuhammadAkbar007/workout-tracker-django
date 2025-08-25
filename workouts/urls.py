from rest_framework.routers import DefaultRouter
from workouts.views import WorkoutViewSet

router = DefaultRouter()
router.register("", WorkoutViewSet, basename="workout")

urlpatterns = router.urls
