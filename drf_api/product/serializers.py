from rest_framework import serializers
from .models import Product
from category.serializers import CategorySerializer
from motocycleImage.serializers import MotocycleSerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = MotocycleSerializer(many=True, read_only=True)  # ← FIXED HERE

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'posted_by']

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['posted_by'] = request.user
        return super().create(validated_data)
