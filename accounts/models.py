from django.db import models
from django.contrib.auth.models import User

# class Profile to complete user sign up information

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    gender = models.CharField(max_length = 20)
    state = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length = 35)
    block_call = models.CharField(max_length = 15, unique = True)
    block_sms = models.CharField(max_length = 15, unique = True)
    block_email = models.CharField(max_length = 15, unique = True)


    def __str__(self) -> str:
        return str(self.user)
     

