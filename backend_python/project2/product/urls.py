from django.contrib import admin
from django.urls import path
from .views import RegisterProductAPI,PostViewSet,ProductUpdate,productDelete,productListAPI,productDetail,productListFilterAPI
urlpatterns = [
path("add-product/",RegisterProductAPI.as_view() ),
path("update-product/<int:pk>/",ProductUpdate.as_view()),
path("delete-product/<int:pk>/",productDelete.as_view()),
path("detail-product/<int:pk>/",productDetail.as_view()),

path("list-product/",productListAPI.as_view()),

path("list-product/filter/",productListFilterAPI.as_view())

]