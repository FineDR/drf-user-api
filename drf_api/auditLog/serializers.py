from rest_framework import serializers
from .models import AuditLog
from api.serializers import UserTBSerializer
from contract.serializers import ContractSerializer
from django.contrib.auth import get_user_model

User = get_user_model
class AuditLogSerializer(serializers.ModelSerializer):


    class Meta:
        model = AuditLog
        fields = ['id', 'contract', 'action_type', 'description', 'timestamp']

    def create(self, validated_data):

        request=self.context.get('request')
        if not request or not request.user.is_authenticated:
            raise serializers.ValidationError({"error": "User must be authenticated."})
        validated_data['user']=request.user
        return super().create(validated_data)