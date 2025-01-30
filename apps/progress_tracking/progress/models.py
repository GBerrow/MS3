from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TrainingPlan(models.Model):
    CATEGORY_CHOICES = [
        ('WEIGHT_LOSS', 'Weight Loss'),
        ('MUSCLE_GAIN', 'Muscle Gain'), 
        ('STRENGTH', 'Strength Training'),
        ('WELLNESS', 'Overall Wellness'),
        ('CARDIO', 'Cardio Fitness'),
        ('BEGINNER', 'Beginner Friendly')
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    duration_weeks = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class WorkoutLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    training_plan = models.ForeignKey(TrainingPlan, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    duration = models.DurationField()
    notes = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
