from drf_api.base import BaseListCreateAPIView,BaseRetrieveUpdateDestroyAPIView

from .models import Message

from .serializers import MessageSerializer

class MessageCreateListAPIView(BaseListCreateAPIView):
    model = Message
    serializer_class = MessageSerializer


    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)



class MessageRetrieveUpdateDestroyAPIView(BaseRetrieveUpdateDestroyAPIView):
    model = Message
    serializer_class = MessageSerializer