from django.db import models
from user.models import User

# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_user')
    subject = models.CharField(max_length=50, blank=True, null=True)
    experience_years = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}. {self.user.first_name} | {self.user.last_name}"
