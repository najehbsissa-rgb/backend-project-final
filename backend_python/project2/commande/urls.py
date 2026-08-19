from django.urls import path

from .views import (
    CommandeListView,
    CommandeDetailView
)


urlpatterns = [

    path(
        'commandes/',
        CommandeListView.as_view(),
        name='commande-list'
    ),

    path(
        'commandes/<int:id>/',
        CommandeDetailView.as_view(),
        name='commande-detail'
    ),

]