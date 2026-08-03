from django.contrib import admin
from django.urls import path
from .views import user1ListAPI

urlpatterns = [
    path('user1-list/',user1ListAPI.as_view() ,name=" user1 list"),
]