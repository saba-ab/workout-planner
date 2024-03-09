from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'exercise', views.ExerciseViewSet)
router.register(r'workoutplans', views.WorkoutPlanViewSet)
router.register(r'progresstracking', views.ProgressTrackingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
