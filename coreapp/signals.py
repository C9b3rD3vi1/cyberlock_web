
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print("Signal triggered: Creating profile...")
        Profile.objects.create(user=instance)


"""
This function is a signal receiver that is triggered when a User object is saved.
Its purpose is to ensure that the associated Profile object for the User is also saved.

Parameters:
- `sender`: The model class that triggered the signal. In this case, it is the `User` model.
- `instance`: The instance of the model that triggered the signal. It is the specific `User` object that was saved.
- `**kwargs`: Additional keyword arguments that may be passed to the signal receiver.

The function does not return any value. It simply saves the associated Profile object for the given User instance.
"""

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
