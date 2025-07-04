from django.db import models
from api.models import UserTB
from conversation.models import Conversation

class Message(models.Model):
    id=models.AutoField(primary_key=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(UserTB, on_delete=models.CASCADE, related_name='sent_messages', default=1)
    message_description = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender.username} at {self.sent_at}'
