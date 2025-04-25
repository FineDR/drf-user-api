from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Contract

User = get_user_model()

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'contract_type', 'start_date', 'end_date', 'status', 'payment_frequency', 'total_amount', 'created_at']

    def create(self, validated_data):
        request = self.context.get('request')  # Pata request kutoka context
        if not request or not request.user.is_authenticated:
            raise serializers.ValidationError({"error": "User must be authenticated."})

        validated_data['boss'] = request.user  
        validated_data['rider'] = request.user  

        return super().create(validated_data)
