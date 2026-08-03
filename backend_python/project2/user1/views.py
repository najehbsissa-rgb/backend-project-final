from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User1
class user1ListAPI(APIView):
    def get(self ,request):
          users=User1.objects.all()
          return Response(users, status=status.HTTP_200_OK)
# Create your views here.
