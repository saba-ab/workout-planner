from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'exercises', views.ExerciseViewSet)
router.register(r'workoutplans', views.WorkoutPlanViewSet,
                basename='workoutplan')
router.register(r'progresstracking',
                views.ProgressTrackingViewSet, basename='progresstracking')
urlpatterns = [
    path('', include(router.urls)),
]
