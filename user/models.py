from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Role(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    TEACHER = 'teacher', 'Teacher'
    STUDENT = 'student', 'Student'

class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='user-profile/', blank=True, null=True)
    email = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)

    def __str__(self):
        return f"{self.id}. {self.first_name} | {self.last_name}"