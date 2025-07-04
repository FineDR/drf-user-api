from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from api.models import UserTB

UserTB =get_user_model()
class Category(models.Model):
    id=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=255)
    created_by=models.ForeignKey(UserTB,on_delete=models.CASCADE,related_name='category_created_by')
    created_at=models.DateTimeField(default=timezone.now)



    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name