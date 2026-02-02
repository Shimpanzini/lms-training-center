from django.db import models
from teacher.models import Teacher

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=20)
    info = models.TextField(blank=True, null=True)
    duration = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

