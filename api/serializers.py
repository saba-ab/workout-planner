from rest_framework import serializers
from .models import Exercise, WorkoutPlan, WorkoutPlanExercise, ProgressTracking


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        name = WorkoutPlan
        fields = '__all__'


# class WorkoutPlanExerciseSerializer(serializers.ModelSerializer):
#     class Meta:
#         name = WorkoutPlanExercise
#         fields = '__all__'


class ProgressTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        name = ProgressTracking
        fields = '__all__'
