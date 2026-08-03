from django.db import models
class Vol(models.Model):
   numerodeVol = models.IntegerField()
   contact=models.CharField(max_length=200)
   departDate=models.DateField()
   nombrePassage=models.IntegerField()
   prixTicket=models.FloatField()
   def __str__(self):
       return self.numerodeVol
# Create your models here.
