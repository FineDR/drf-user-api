from django.urls import path

from . import views

urlpatterns=[
    path('',views.AssetsListCreateAPIView.as_view(),name='asset-list-create'),
    path('<int:pk>/',views.AssetsDetailAPIView.as_view(),name='asset-detail')
]