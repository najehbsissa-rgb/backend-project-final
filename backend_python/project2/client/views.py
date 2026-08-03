from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ClientSerializers,ClientLoginSerializer
from  .models import Client
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterClientAPI(APIView):
    def post(self,request):
        client=ClientSerializers(data=request.data)
        if client.is_valid():
              client.save()
              return Response(data=client.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=client.errors, status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth.hashers import check_password

class LoginClientAPI(APIView):
    def post(self, request):
        serializer = ClientLoginSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            try:
                client = Client.objects.get(email=email)
            except Client.DoesNotExist:
                return Response(
                    {"message": "Invalid email or password"},
                    status=status.HTTP_401_UNAUTHORIZED
                )

            if check_password(password, client.password):
                refresh = RefreshToken.for_user(client)

                return Response({
                   'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    "id": client.id,
                    "email": client.email,
                    "identifier": client.identifier,
                }, status=status.HTTP_200_OK)

            return Response(
                {"message": "Invalid email or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
