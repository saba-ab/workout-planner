from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()
    target_muscles = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class WorkoutPlan(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='workout_plans')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    exercises = models.ManyToManyField(Exercise, through='WorkoutPlanExercise')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} by {self.user.username}"


class WorkoutPlanExercise(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    repetitions = models.PositiveIntegerField()
    sets = models.PositiveIntegerField()
    duration = models.DurationField(blank=True, null=True)

    class Meta:
        unique_together = [
            ['workout_plan', 'exercise']
        ]


class ProgressTracking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='progress_tracking')
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    workout_plan = models.ForeignKey(
        WorkoutPlan, on_delete=models.SET_NULL, null=True, blank=True, related_name='progress_entries')
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"progress for  {self.user.username} on {self.date}"
