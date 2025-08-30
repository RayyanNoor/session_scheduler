from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    timezone = models.CharField(max_length=100, default="UTC")
    meeting_link = models.URLField(blank=True, null=True)
