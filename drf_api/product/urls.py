from django.urls import path

from .views import ProductCreateListAPIView, ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', ProductCreateListAPIView.as_view(), name='product-list-create'),
    path('<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),
]