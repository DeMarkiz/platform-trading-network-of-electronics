from django.contrib.auth.models import AbstractUser
from django.db import models




class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []