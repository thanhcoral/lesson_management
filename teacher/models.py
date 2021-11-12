from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Teacher(User):
    years_of_experience = models.IntegerField()
    