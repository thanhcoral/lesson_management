from django.db import models
from teacher.models import Teacher
from student.models import Student
# Create your models here.
class Lesson(models.Model):
    name = models.CharField(max_length=50, null=False)
    time = models.CharField(max_length=50, null=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="lesson_teacher")
    students = models.ManyToManyField(Student)