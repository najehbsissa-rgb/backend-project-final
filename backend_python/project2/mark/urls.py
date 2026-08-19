from django.urls import path

from .views import (
    MarkAPIView,
    MarkCreateAPIView,
    MarkDetailAPIView,
    MarkUpdateAPIView,
    MarkDeleteAPIView
)

urlpatterns = [

    # GET liste
    path(
        'marks/',
        MarkAPIView.as_view(),
        name='mark-list'
    ),

    # POST créer
    path(
        'marks/create/',
        MarkCreateAPIView.as_view(),
        name='mark-create'
    ),

    # GET détail
    path(
        'marks/<int:id>/',
        MarkDetailAPIView.as_view(),
        name='mark-detail'
    ),

    # PUT modifier
    path(
        'marks/<int:id>/update/',
        MarkUpdateAPIView.as_view(),
        name='mark-update'
    ),

    # DELETE supprimer
    path(
        'marks/<int:id>/delete/',
        MarkDeleteAPIView.as_view(),
        name='mark-delete'
    ),
]