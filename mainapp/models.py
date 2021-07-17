from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()


class User(AbstractUser):
    image = models.ImageField(blank=True)
