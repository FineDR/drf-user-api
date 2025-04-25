from django.db import models
from contract.models import Contract
from django.conf import settings

class Assets(models.Model):
    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('In Contract', 'In Contract'),
        ('Returned', 'Returned'),
    )
    id = models.AutoField(primary_key=True)
    boss = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="assets", on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, related_name="assets", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    plate_number = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Available')  # Changed max_length to 12
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
