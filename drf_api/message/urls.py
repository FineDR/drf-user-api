from django.urls import path

from .views import MessageCreateListAPIView, MessageRetrieveUpdateDestroyAPIView

urlpatterns=[
    path('', MessageCreateListAPIView.as_view(), name='message-list-create'),
    path('<int:pk>/', MessageRetrieveUpdateDestroyAPIView.as_view(), name='message-retrieve-update-destroy'),
]