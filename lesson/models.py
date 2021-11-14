from django.db import models

from teacher.models import Teacher
from student.models import Student

class Lesson(models.Model):
    name = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='lesson_teacher')
    students = models.ManyToManyField(Student)