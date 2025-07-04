from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
        read_only_fields=['id','created_at','created_by']


    def create(self, validated_data):
        request=self.context.get('request')
        if request and hasattr(request,'user'):
           validated_data['created_by']=request.user
        return super().create(validated_data)