from django.db import models
from django.conf import settings


class Contract(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Terminated', 'Terminated'),
    )

    PAYMENT_FREQUENCY_CHOICES = (
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
    )
    id = models.AutoField(primary_key=True)
    boss = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="contracts_as_boss", on_delete=models.CASCADE)
    rider = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="contracts_as_rider", on_delete=models.CASCADE)
    contract_type=models.CharField(max_length=255)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='Active')
    payment_frequency = models.CharField(max_length=7, choices=PAYMENT_FREQUENCY_CHOICES)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contract {self.id} - {self.status}"