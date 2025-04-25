from django.db import models

# Create your models here.
from django.conf import settings
from contract.models import Contract

class Notification(models.Model):
    TYPE_CHOICES = (
        ('Payment Reminder', 'Payment Reminder'),
        ('Contract Expiry', 'Contract Expiry'),
        ('Missed Payment', 'Missed Payment'),
    )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="notifications", on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, related_name="notifications", on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification {self.id} - {self.type}"