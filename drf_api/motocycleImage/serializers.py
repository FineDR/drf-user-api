from rest_framework import serializers

from .models import MotocycleImage


class MotocycleSerializer(serializers.ModelSerializer):
    class Meta:
        model=MotocycleImage
        fields='__all__'
        read_only_fields=['id','uploaded_at']



    def create(self,validated_data):
        request=self.context.get('request')
        if request and hasattr(request,'user'):
            validated_data['moto']=request.user
        return super().create(validated_data)