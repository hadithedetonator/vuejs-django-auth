# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    skills = models.JSONField(default=dict, blank=True)  # For user skills as JSON
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
