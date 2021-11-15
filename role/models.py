from django.db import models
from django.contrib.auth.models import User

# Create your models here.
ROLES = [
    ('Admin', 'Admin'),
    ('Teacher', 'Teacher'),
    ('Student', 'Student')
]
class Role(models.Model):
    user = models.OneToOneField(User, related_name='role', on_delete=models.CASCADE, unique=True)
    role = models.CharField(choices=ROLES, default='Admin', max_length=20)