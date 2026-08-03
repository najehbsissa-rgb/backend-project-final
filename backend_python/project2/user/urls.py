"""
URL configuration for project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import userListAPI,userHello,CreateUserAPI,usergetById,userUpdate,userDelete

urlpatterns = [
    path('user-list/',userListAPI.as_view() ,name=" user list"),
    path('user-hello',userHello.as_view() , name=" hello user"),
    path('user-create',CreateUserAPI.as_view() , name="create user"),
    path('user-detail/<int:pk>/',usergetById.as_view() , name="create user"),
    path('user-update/<int:pk>/',userUpdate.as_view() , name="update user"),
    path('user-delete/<int:pk>/',userDelete.as_view() , name="delete user"),




    
]