from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Categorie
from .serializers import CategorieSerializer


class CategorieAPIView(APIView):

    # GET : afficher toutes les catégories
    def get(self, request):
        categories = Categorie.objects.all()
        serializer = CategorieSerializer(categories, many=True)

        return Response(serializer.data)

class CategorieCreateAPIView(APIView):
    def post(self, request):
        serializer = CategorieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class CategorieDetailAPIView(APIView):

    # GET : afficher une catégorie
    def get(self, request, id):
        try:
            categorie = Categorie.objects.get(id=id)
        except Categorie.DoesNotExist:
            return Response(
                {"message": "Categorie introuvable"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CategorieSerializer(categorie)
        return Response(serializer.data)


class CategorieUpdateAPIView(APIView):
    def put(self, request, id):
        try:
            categorie = Categorie.objects.get(id=id)
        except Categorie.DoesNotExist:
            return Response(
                {"message": "Categorie introuvable"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CategorieSerializer(
            categorie,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class CategorieDetailAPIView(APIView):
        def get(self,request,pk):
                    categaorie = get_object_or_404(Categorie, id=pk)
                    categorieSerializer=CategorieSerializer(categaorie)
                    return Response(categorieSerializer.data )

class CategorieDeleteAPIView(APIView):
    def delete(self, request, id):
        try:
            categorie = Categorie.objects.get(id=id)
        except Categorie.DoesNotExist:
            return Response(
                {"message": "Categorie introuvable"},
                status=status.HTTP_404_NOT_FOUND
            )

        categorie.delete()

        return Response(
            {"message": "Categorie supprimée"},
            status=status.HTTP_204_NO_CONTENT
        )