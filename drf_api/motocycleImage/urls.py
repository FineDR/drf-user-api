from django.urls import path

from .views import MotocycleListCreateAPIView, MotocycleRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', MotocycleListCreateAPIView.as_view(), name='motocycle-image-list-create'),
    path('<int:pk>/', MotocycleRetrieveUpdateDestroyAPIView.as_view(), name='motocycle-image-retrieve-update-destroy'),
]
# This code defines the URL patterns for the motocycle image API. It includes two endpoints: