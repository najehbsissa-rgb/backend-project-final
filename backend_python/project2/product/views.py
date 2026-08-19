from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

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



class ProductUpdate(APIView):

    def patch(self, request, pk):
        print(pk)
        product = get_object_or_404(Product, id=pk)

        product_serializer = ProductSerializer(
            product,
            data=request.data,
            partial=True
        )

        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)

        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        product_serializer = ProductSerializer(
            product,
            data=request.data
        )

        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)

        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class productDelete(APIView):
    def delete(self,request,pk):
                    product = get_object_or_404(Product, id=pk)
                    product.delete()
        
                    return Response(
                        {"msg": "Le produit a été supprimé avec succès."}, 
                        status=status.HTTP_200_OK # Le statut HTTP doit être passé dans l'argument 'status' de Response
                    )


class productListAPI(APIView):
    def get(self ,request):
        product=Product.objects.all()
        product_serializer = ProductSerializer(product, many=True)
        return Response( product_serializer.data, status=status.HTTP_200_OK)                  
class productDetail(APIView):
        def get(self,request,pk):
                    product = get_object_or_404(Product, id=pk)
                    product_serializer=ProductSerializer(product)
                    return Response(product_serializer.data
                    )
class productListFilterAPI(APIView):
    def get(self ,request):
        product=Product.objects.all()
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['identifier', 'nameProduct', 'priceUnitaire']
        product_serializer = ProductSerializer(product, many=True)
        return Response( product_serializer.data, status=status.HTTP_200_OK)     