from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    force_change_password = models.BooleanField()


def create_user_profile(sender, instance, created, **kwargs):
    # refer to https://docs.djangoproject.com/en/dev/topics/auth/#django.contrib.auth.models.UserManager.create_user
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
