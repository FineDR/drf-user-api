from rest_framework import serializers
from .models import Notification
from django.contrib.auth import get_user_model

User = get_user_model()

class NotificationSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Notification
        fields = ['id', 'contract', 'message', 'type', 'is_read', 'created_at']

    def create(self, validated_data):
        request = self.context.get('request')

        if not request or not request.user.is_authenticated:
            raise serializers.ValidationError({"error": "User must be authenticated."})
        
        validated_data['user'] = request.user
        return super().create(validated_data)
