from django.db import models
from api.models import UserTB
from product.models import Product

class Conversation(models.Model):
    id=models.AutoField(primary_key=True)
    CONVERSATION_CHOICE = [
        ('read', 'Read'),
        ('unread', 'Unread')
    ]

    moto = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_conversations')
    buyer = models.ForeignKey(UserTB, on_delete=models.CASCADE, related_name="conversations_as_buyer")
    seller = models.ForeignKey(UserTB, on_delete=models.CASCADE, related_name="conversations_as_seller",default=1)
    started_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CONVERSATION_CHOICE, default="unread")

    def __str__(self):
        return f'{self.moto.title} - {self.buyer.username} to {self.seller.username}'
