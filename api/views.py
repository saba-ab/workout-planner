from django.shortcuts import render
from rest_framework import viewsets
from .models import Exercise, WorkoutPlan, ProgressTracking
from .serializers import ExerciseSerializer, WorkoutPlanSerializer, ProgressTrackingSerializer
# Create your views here.


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer


class ProgressTrackingViewSet(viewsets.ModelViewSet):
    queryset = ProgressTracking.objects.all()
    serializer_class = ProgressTrackingSerializer
