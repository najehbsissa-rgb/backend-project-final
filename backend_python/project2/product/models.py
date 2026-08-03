from django.db import models
from categorie.models import Categorie
from mark.models import Mark

class Product(models.Model):
   identifier = models.CharField(max_length=40, unique=True)
   nameProduct = models.CharField(max_length=200 ,default="identifier" , null=True)
   designationProduct=models.CharField(max_length=200 ,default="ddd", null=True)
   priceUnitaire=models.IntegerField( default=0 ,null=True)
   tva=models.FloatField(null=True)
   prixttc=models.FloatField(null=True)
   totalMontant=models.FloatField(null=True)
   id_categorie=models.ForeignKey(
        Categorie,                      # Related model
        on_delete=models.CASCADE,  # Delete related rows when User is deleted
        related_name="categories" ,null=True      # Reverse relation name
      )
   id_mark=models.ForeignKey(
        Mark,                      # Related model
        on_delete=models.CASCADE,  # Delete related rows when User is deleted
        related_name="marks" ,null=True      # Reverse relation name
    )

   def __str__(self):
       return self.nameProduct
# Create your models here.
