from django.contrib import admin
from django.urls import path
from .views import RegisterClientAPI,LoginClientAPI
urlpatterns = [
path("register/",RegisterClientAPI.as_view() ),
path("login/",LoginClientAPI.as_view() ),

]