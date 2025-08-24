from rest_framework.routers import DefaultRouter

from exercises.views import ExerciseViewSet

router = DefaultRouter()
router.register("", ExerciseViewSet, basename="exercise")

urlpatterns = router.urls
