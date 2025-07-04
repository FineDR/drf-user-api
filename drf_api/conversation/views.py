from drf_api.base import BaseListCreateAPIView,BaseRetrieveUpdateDestroyAPIView

from .serializers import ConversationSerializer
from .models import Conversation


class ConversationListCreateAPIView(BaseListCreateAPIView):
    model = Conversation
    serializer_class = ConversationSerializer

class ConversationRetrieveUpdateDestroyAPIView(BaseRetrieveUpdateDestroyAPIView):
    model = Conversation
    serializer_class = ConversationSerializer
    