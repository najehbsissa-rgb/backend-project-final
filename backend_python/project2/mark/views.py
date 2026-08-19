from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Mark
from .serializers import MarkSerializer


# =========================
# GET : liste des marques
# =========================
class MarkAPIView(APIView):

    def get(self, request):
        marks = Mark.objects.all()
        serializer = MarkSerializer(marks, many=True)

        return Response(serializer.data)


# =========================
# POST : créer une marque
# =========================
class MarkCreateAPIView(APIView):

    def post(self, request):
        serializer = MarkSerializer(data=request.data)

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


# =========================
# GET : détail d'une marque
# =========================
class MarkDetailAPIView(APIView):

    def get(self, request, id):

        try:
            mark = Mark.objects.get(id=id)

        except Mark.DoesNotExist:
            return Response(
                {"message": "Mark introuvable"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MarkSerializer(mark)

        return Response(serializer.data)


# =========================
# PUT : modifier une marque
# =========================
class MarkUpdateAPIView(APIView):

    def put(self, request, id):

        try:
            mark = Mark.objects.get(id=id)

        except Mark.DoesNotExist:
            return Response(
                {"message": "Mark introuvable"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MarkSerializer(
            mark,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# =========================
# DELETE : supprimer une marque
# =========================
class MarkDeleteAPIView(APIView):

    def delete(self, request, id):

        try:
            mark = Mark.objects.get(id=id)

        except Mark.DoesNotExist:
            return Response(
                {"message": "Mark introuvable"},
                status=status.HTTP_404_NOT_FOUND
            )

        mark.delete()

        return Response(
            {"message": "Mark supprimée"},
            status=status.HTTP_204_NO_CONTENT
        )