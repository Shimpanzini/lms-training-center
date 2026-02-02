from django.db import models
from student.models import Student
from teacher.models import Teacher
from subject.models import Course

# Create your models here.


class Group(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    group = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    max_students = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course.name


class Homework(models.Model):
    group = models.ForeignKey("group.Group", on_delete=models.CASCADE)
    homework = models.TextField(blank=True, null=True)
    content = models.FileField(upload_to='homework/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.group


class HomeworkSubmissions(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    content = models.FileField(upload_to='student-homework/', blank=True, null=True)
    content_text = models.TextField(blank=True, null=True)
    score = models.IntegerField(default=0)
    teacher_commit = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.user.username
    

class Status(models.TextChoices):
    ACTIVE = 'active', ' Active'
    FINISHED = 'finished', 'Finished'
    DROPED = 'droped', 'Droped'

class Enrollman(models.Model):
    