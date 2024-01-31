from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=8000)
    created_at = models.DateTimeField(default=timezone.now)
