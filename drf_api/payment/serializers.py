from rest_framework import serializers
from .models import Payment
from django.contrib.auth import get_user_model

User= get_user_model

class PaymentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Payment
        fields = ['id', 'contract', 'amount_paid', 'payment_date', 'status', 'transaction_id', 'created_at']


    def create(self, validated_data):
        

        request=self.context.get('request')

        if not request or not request.user.is_authenticated:
            raise serializers.ValidationError({"user":"user must be authenticated"})
        
        validated_data['rider']=request.user
        return super().create(validated_data)