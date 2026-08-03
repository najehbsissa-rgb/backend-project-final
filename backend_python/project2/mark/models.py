from django.db import models
class Mark(models.Model):
    identifier = models.CharField(max_length=40, unique=True)
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
   
# Create your models here.
