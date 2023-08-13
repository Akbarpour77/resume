from django.db import models
from user_auth_app.models import UserProfile


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    created_at = models.DateField()
    updated_at = models.DateField()
    user_id = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
