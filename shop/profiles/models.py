from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    country = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=64, blank=True)
    street = models.CharField(max_length=64, blank=True)
    house = models.CharField(max_length=64, blank=True)
    flat = models.CharField(max_length=64, blank=True)

