from rest_framework import serializers
from .models import Exercise, WorkoutPlan, WorkoutPlanExercise, ProgressTracking
from django.contrib.auth.models import User


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'
        read_only_fields = ['user']


# class WorkoutPlanExerciseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WorkoutPlanExercise
#         fields = '__all__'


class ProgressTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressTracking
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
