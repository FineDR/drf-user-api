from django.db import models
from contract.models import Contract
# Create your models here.
from django.conf import settings

class AuditLog(models.Model):
    ACTION_CHOICES = (
        ('Created', 'Created'),
        ('Updated', 'Updated'),
        ('Deleted', 'Deleted'),
    )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="audit_logs", on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, related_name="audit_logs", on_delete=models.CASCADE)
    action_type = models.CharField(max_length=10, choices=ACTION_CHOICES)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AuditLog {self.id} - {self.action_type}"