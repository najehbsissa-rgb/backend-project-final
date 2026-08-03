from django.contrib import admin
from django.urls import path
from .views import RegisterProductAPI,PostViewSet
urlpatterns = [
path("add-product/",RegisterProductAPI.as_view() ),

]