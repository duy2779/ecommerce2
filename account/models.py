from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from uuid import uuid4

# Create your models here.


def path_and_rename(instance, filename):
    filebase, extension = filename.split('.')
    return '%s.%s' % (instance.username, extension)


class User(AbstractUser):
    first_name = None
    last_name = None
    full_name = models.CharField(max_length=200)

    avatar = models.ImageField(
        upload_to=path_and_rename, default="avatar.png")
    email = models.EmailField(max_length=100, unique=True)
