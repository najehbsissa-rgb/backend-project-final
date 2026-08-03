from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
class userListAPI(APIView):
    def get(self ,request):
        users=User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
class userHello(APIView):
    def get(self,request):
        return Response(' hello world')
class CreateUserAPI(APIView):
    def post(self, request):
        userSerializer = UserSerializer(data=request.data)
        
        # 1. Appel de la méthode avec des parenthèses ()
        if userSerializer.is_valid():
            userSerializer.save()
            # 2. Syntaxe de dictionnaire corrigée et code statut adapté (211 Created)
            return Response(data=userSerializer.data, status=status.HTTP_201_CREATED)
        else:
            # 3. Retour des erreurs de validation et code statut corrigé
            return Response(data=userSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

class usergetById(APIView):
    def get(self ,request ,pk):
        user = get_object_or_404(User, id=pk)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)

class userUpdate(APIView):
    def patch(self,request,pk):
        user = get_object_or_404(User, id=pk)
        if user:
                    user_serializer = UserSerializer( user ,data=request.data , partial=True)
                    if user_serializer.is_valid():

                        user_serializer.save()
                        return Response(user_serializer.data,status=status.HTTP_200_OK)
        else:
             return Response(status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
            user = get_object_or_404(User, id=pk)
            if user:
                        user_serializer = UserSerializer( user ,data=request.data )
                        if user_serializer.is_valid():

                            user_serializer.save()
                            return Response(user_serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
class userDelete(APIView):
    def delete(self,request,pk):
                    user = get_object_or_404(User, id=pk)
                    user.delete()
        
                    return Response(
                        {"msg": "L'utilisateur a été supprimé avec succès."}, 
                        status=status.HTTP_200_OK # Le statut HTTP doit être passé dans l'argument 'status' de Response
                    )

