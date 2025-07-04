from django.db import models
from category.models import Category
from api.models import UserTB

class Product(models.Model):
    PRODUCT_CHOICE_STATUS = [
        ("available", "Available"),
        ("sold", "Sold"),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_of_product')
    posted_by = models.ForeignKey(UserTB, on_delete=models.CASCADE, related_name='product_posted_by')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=PRODUCT_CHOICE_STATUS, default="available")

    def __str__(self):
        return f"{self.title} - {self.status}"
