from django.urls import path

from .views import (
    CategorieAPIView,
    CategorieCreateAPIView,
    CategorieDetailAPIView,
    CategorieUpdateAPIView,
    CategorieDeleteAPIView
)

urlpatterns = [

    # GET : liste des catégories
    path(
        'categories/',
        CategorieAPIView.as_view(),
        name='categorie-list'
    ),

    # POST : créer une catégorie
    path(
        'categories/create/',
        CategorieCreateAPIView.as_view(),
        name='categorie-create'
    ),

    # GET : détail d'une catégorie
    path(
        'categories/<int:id>/',
        CategorieDetailAPIView.as_view(),
        name='categorie-detail'
    ),

    # PUT : modifier une catégorie
    path(
        'categories/<int:id>/update/',
        CategorieUpdateAPIView.as_view(),
        name='categorie-update'
    ),

    # DELETE : supprimer une catégorie
    path(
        'categories/<int:id>/delete/',
        CategorieDeleteAPIView.as_view(),
        name='categorie-delete'
    ),
    path(
        'categories/<int:pk>/detail/',
        CategorieDetailAPIView.as_view(),
        name='categorie-detail'

    )
]