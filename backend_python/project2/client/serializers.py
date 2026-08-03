from rest_framework import serializers
from .models import Client
class ClientSerializers(serializers.ModelSerializer):
      class Meta:
        model = Client
        fields = '__all__'

      def create(self,validated_data):
        password=validated_data.pop("password")
        client=Client(**validated_data)
        client.set_password(password)
        client.save()
        return  client
class ClientLoginSerializer(serializers.Serializer):
    email=serializers.CharField()
    password=serializers.CharField()
    