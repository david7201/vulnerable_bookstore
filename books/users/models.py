# users/models.py
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

# users/models.py (final version)
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='userprofile'
    )
    name = models.CharField(max_length=100)
    secret_info = models.TextField(blank=True)

    def __str__(self):
        return self.name

