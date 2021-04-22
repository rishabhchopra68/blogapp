from django.db.models.signals import post_save # signal that gets fired when object is saved

from django.contrib.auth.models import User # user here is sender, since it sends a signal

# we also need a reciever
from django.dispatch import receiver
from .models import Profile

@receiver(post_save , sender = User)
def create_profile(sender , instance , created , **kwargs): # this function is the receiver
    if created :
        Profile.objects.create(user = instance)


@receiver(post_save , sender = User)            # saving the created profile
def save_profile(sender , instance , **kwargs): 
    instance.profile.save()