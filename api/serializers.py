from rest_framework import serializers
from .models import Exercise, WorkoutPlan, WorkoutPlanExercise, ProgressTracking
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

User = get_user_model()


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'instructions',
                  'target_muscles']


class WorkoutPlanSerializer(serializers.ModelSerializer):
    exercises = serializers.PrimaryKeyRelatedField(
        queryset=Exercise.objects.all(), many=True)

    class Meta:
        model = WorkoutPlan
        fields = ['name', 'exercises', 'user']
        read_only_fields = ['user']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorkoutPlanExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlanExercise
        fields = ['id', 'workout_plan', 'exercise',
                  'repetitions', 'sets', 'duration']


class ProgressTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressTracking
        fields = ['id', 'user', 'date', 'weight', 'workout_plan', 'notes']
        read_only_fields = ['user']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.password = make_password(password)
        return super(UserSerializer, self).update(instance, validated_data)
