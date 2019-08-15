from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    # profile_image = models.ImageField(upload_to="users/profile_pic", blank=True)
    is_pastor = models.BooleanField(default=True)
