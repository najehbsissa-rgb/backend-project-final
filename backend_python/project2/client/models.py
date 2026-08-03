from django.db import models
from user.models import User
from django.contrib.auth.models import AbstractBaseUser
class Client(AbstractBaseUser):
    identifier = models.CharField(max_length=40, unique=True)
    adresse=models.CharField(max_length=200)
    ville=models.CharField(max_length=200)
    email=models.EmailField()
    # id_user = models.ForeignKey(
    #     User,                      # Related model
    #     on_delete=models.CASCADE,  # Delete related rows when User is deleted
    #     related_name="users"       # Reverse relation name
    # )

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['identifier', 'ville']


    
