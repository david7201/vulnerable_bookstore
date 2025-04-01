# update_profiles.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore_project.settings")
django.setup()

from django.contrib.auth import get_user_model
from users.models import UserProfile

User = get_user_model()

for profile in UserProfile.objects.filter(user__isnull=True):
    try:
        # Assuming you previously stored the old user ID in some field,
        # or you can use another method to get the correct user.
        # Here we assume you still have the user ID saved in an attribute.
        old_user_id = profile.__dict__.get("user_id")
        user = User.objects.get(pk=old_user_id)
        profile.user = user
        profile.save()
        print(f"Updated profile for user id {old_user_id}")
    except Exception as e:
        print(f"Error updating profile for user id {old_user_id}: {e}")
