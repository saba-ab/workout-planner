from django.shortcuts import render
from rest_framework import viewsets, status, generics
from .models import Exercise, WorkoutPlan, ProgressTracking
from .serializers import ExerciseSerializer, WorkoutPlanSerializer, ProgressTrackingSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]


class WorkoutPlanViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutPlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WorkoutPlan.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProgressTrackingViewSet(viewsets.ModelViewSet):
    serializer_class = ProgressTrackingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ProgressTracking.objects.filter(user=self.request.user)


class UserCreate(APIView):
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.id, 'username': user.username}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
