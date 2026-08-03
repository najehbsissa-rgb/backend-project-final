from django.db import models
class User1(models.Model):
   firstName = models.CharField(max_length=200)
   lastName=models.CharField(max_length=200)
   email=models.EmailField()
   dateNaissance=models.DateField()
   def __str__(self):
       return self.firstName

# Create your models here.
