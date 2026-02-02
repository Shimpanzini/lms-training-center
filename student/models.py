from django.db import models
from user.models import User
# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    birthday = models.DateField(blank=True, null=True)
    level = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}. {self.user.first_name} | {self.user.last_name}"



class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey("group.Group", on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)
    attendance_date = models.DateField()

    def __str__(self):
        return self.student.user.username
    
