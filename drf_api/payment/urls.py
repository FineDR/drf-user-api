from django.urls import path
from . import views

urlpatterns = [
    path('', views.PaymentListCreateAPIView.as_view(), name='payment-list-create'), 
    path('<int:pk>/',views.PaymentDetailAPIView.as_view(), name='payment-detail'), 
    path('<int:id>/approve/',views.PaymentApprovalAPIView.as_view(), name='payment-approve'), 
]
