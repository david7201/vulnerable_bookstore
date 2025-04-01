# users/signals.py
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Automatically create a profile with the user's username
        UserProfile.objects.create(user=instance, name=instance.username)
