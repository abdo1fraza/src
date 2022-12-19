from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# class Profile to complete user sign up information

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    gender = models.CharField(max_length = 20)
    state = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length = 35)
    block_call = models.CharField(max_length = 15, unique = True)
    block_sms = models.CharField(max_length = 15, unique = True)
    block_email = models.CharField(max_length = 15, unique = True)


    def __str__(self):
        return str(self.user)
     

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kargw):
    if created:
        Profile.objects.create(
            user = instance
        )

