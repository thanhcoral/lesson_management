from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(User):
    address = models.CharField(max_length=200)