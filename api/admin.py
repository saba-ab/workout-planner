from django.contrib import admin
from .models import Exercise, WorkoutPlan, WorkoutPlanExercise, ProgressTracking
# Register your models here.

admin.site.register(Exercise)
admin.site.register(WorkoutPlan)
admin.site.register(WorkoutPlanExercise)
admin.site.register(ProgressTracking)
