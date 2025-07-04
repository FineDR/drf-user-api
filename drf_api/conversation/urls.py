from django.urls import path
from .views import ConversationListCreateAPIView, ConversationRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('', ConversationListCreateAPIView.as_view(), name='conversation-list-create'),
    path('<int:pk>/', ConversationRetrieveUpdateDestroyAPIView.as_view(), name='conversation-retrieve-update-destroy'),
]