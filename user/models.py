from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    profile_picture = models.ImageField(default='default_profile_pic.jpg',upload_to='profile_pictures', blank=True)