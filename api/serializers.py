from rest_framework import serializers
from .models import Exercise, WorkoutPlan, WorkoutPlanExercise, ProgressTracking
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description',
                  'instructions', 'target_muscles']


class WorkoutPlanExerciseSerializer(serializers.ModelSerializer):
    exercise_id = serializers.PrimaryKeyRelatedField(
        queryset=Exercise.objects.all(), source='exercise')

    class Meta:
        model = WorkoutPlanExercise
        fields = ['exercise_id', 'repetitions', 'sets', 'duration']


class WorkoutPlanSerializer(serializers.ModelSerializer):
    exercises = WorkoutPlanExerciseSerializer(
        source='workoutplanexercise_set', many=True)
    user = serializers.ReadOnlyField(
        source='user.username')  # Display the username

    class Meta:
        model = WorkoutPlan
        fields = ['id', 'name', 'description', 'exercises', 'user']
        read_only_fields = ['user']

    def create(self, validated_data):
        exercises_data = validated_data.pop('workoutplanexercise_set')
        workout_plan = WorkoutPlan.objects.create(**validated_data)
        for exercise_data in exercises_data:
            WorkoutPlanExercise.objects.create(
                workout_plan=workout_plan, **exercise_data)
        return workout_plan


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
