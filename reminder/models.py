from django.db import models
from django.contrib.auth.models import User
class Reminder(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Adding ForeignKey to User model
    message = models.TextField(max_length=100, null=True, blank=True)
    schedule_time = models.DateTimeField(null=False)  # Adding not null constraint
    created_at = models.DateTimeField(auto_now_add=True, editable=False)  # Renaming timestamp to created_at
    updated_at = models.DateTimeField(auto_now=True)  # Adding updated_at field
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"Reminder - {self.message}"
