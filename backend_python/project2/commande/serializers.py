from rest_framework import serializers
from .models import commande


class CommandeSerializer(serializers.ModelSerializer):

    class Meta:
        model = commande
        fields = '__all__'