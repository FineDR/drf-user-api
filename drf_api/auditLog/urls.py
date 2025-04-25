from django.urls import path

from . import views

urlpatterns=[
    path('',views.AuditLogListCreateAPIView.as_view(),name='log-list-create'),
    path('<int:pk>/',views.AuditLogDetailAPIView.as_view(),name='log-detail'),
]