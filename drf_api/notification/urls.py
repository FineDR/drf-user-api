from django.urls import path

from . import views

urlpatterns=[
    path('',views.NotificationListCreateAPIView.as_view(),name='notification-list-create'),
    path('<int:pk>/',views.NotificationDetailAPIView.as_view(),name='notification-detail'),
]