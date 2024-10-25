# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('backend_developer', 'Backend Developer'),
        ('frontend_developer', 'Frontend Developer'),
        ('qa', 'QA'),
        ('devops', 'DevOps'),
        ('documentation_maestro', 'Documentation Maestro'),
        ('ui/ux', 'UI/UX'),
        ('erd', 'ERD'),
        ('project_manager', 'Project Manager'),
    ]

    bio = models.TextField(null=True, blank=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, null=True, blank=True)
    skills = models.JSONField(default=dict, blank=True)  # For user skills as JSON
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.username