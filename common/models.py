from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    broker_id = models.CharField(max_length=30, blank=True)