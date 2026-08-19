from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import commande
from .serializers import CommandeSerializer


# GET liste + POST
class CommandeListView(APIView):

    def get(self, request):

        commandes = commande.objects.all()

        serializer = CommandeSerializer(
            commandes,
            many=True
        )

        return Response(serializer.data)


    def post(self, request):

        serializer = CommandeSerializer(
            data=request.data
        )

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


# GET détail + PUT + DELETE
class CommandeDetailView(APIView):

    def get(self, request, id):

        cmd = get_object_or_404(
            commande,
            id=id
        )

        serializer = CommandeSerializer(cmd)

        return Response(serializer.data)


    def put(self, request, id):

        cmd = get_object_or_404(
            commande,
            id=id
        )

        serializer = CommandeSerializer(
            cmd,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    def delete(self, request, id):

        cmd = get_object_or_404(
            commande,
            id=id
        )

        cmd.delete()

        return Response(
            {
                "message": "Commande supprimée avec succès"
            },
            status=status.HTTP_204_NO_CONTENT
        )