from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
class RegisterProductAPI(APIView):
    def post(self,request):
        product=ProductSerializer(data=request.data)
        if product.is_valid():
            price_unitaire = product.validated_data.get('priceUnitaire', 0) or 0
            tva = product.validated_data.get('tva', 0) or 0
            calcul_tva = price_unitaire * (tva / 100)
            prix_ttc = price_unitaire + calcul_tva
            product.validated_data['prixttc'] = prix_ttc
            product.save()
            return Response(data=product.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=product.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
   
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
   
    filterset_fields = ['identifier', 'nameProduct', ]
   
    search_fields = ['identifier', 'nameProduct', ]



