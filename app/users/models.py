from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    nickname = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to="user_image", blank=True)
    point = models.PositiveIntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def like_cafes(self):
        return self.cafelike_set.all()