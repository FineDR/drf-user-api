from django.urls import path
from . import views

urlpatterns=[
        path('',views.ContractListCreateAPIView.as_view(),name='contract-list-create'),
        path('<int:pk>/',views.ContractDetailAPIView.as_view(),name='contract-detail')
]