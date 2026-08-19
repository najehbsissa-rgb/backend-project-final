from django.db import models

from product.models import Product
class commande(models.Model):

    identifier = models.CharField(max_length=40, unique=True)
    mtTotal = models.FloatField(null=True)
    mtttc = models.FloatField(null=True)
    tauxTVA = models.FloatField(null=True)
    qunatite = models.FloatField(null=True)
    validation = models.BooleanField(default=False)
    id_product=models.ForeignKey(
        Product,                      # Related model
        on_delete=models.CASCADE,  # Delete related rows when User is deleted
        related_name="products" ,null=True      # Reverse relation name
      )
    def __str__(self):
        return self.identifier