from django.db import models
from django.core.validators import FileExtensionValidator


class MotocycleImage(models.Model):
    id=models.AutoField(primary_key=True)
    image = models.ImageField(
    upload_to='motorcycle_images/',
    validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
    null=True, blank=True
)
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, related_name="images")

    is_primary=models.BooleanField(default=False)
    uploaded_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.image} - {self.is_primary}'

    
