from rest_framework import status,permissions
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.generics import get_object_or_404



class NotificationListCreateAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):
        
        notifications=Notification.objects.all()
        serializer=NotificationSerializer(notifications,many=True)
        return Response(serializer.data)
    
    def post(self,request):

        serializer=NotificationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class NotificationDetailAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,pk):

        notification=get_object_or_404(Notification,pk=pk)
        serializer=NotificationSerializer(notification)
        return Response(serializer.data)
    

    def put(self,request,pk):
       

        notification=get_object_or_404(Notification,pk=pk)
        serializer=NotificationSerializer(notification,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,pk):

        notification=get_object_or_404(Notification,pk=pk)
        notification.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    

