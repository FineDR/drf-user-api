from rest_framework import status,permissions
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import AuditLog
from .serializers import AuditLogSerializer
from rest_framework.generics import get_object_or_404



class AuditLogListCreateAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):
        
        logs=AuditLog.objects.all()
        serializer=AuditLogSerializer(logs,many=True)
        return Response(serializer.data)
    
    def post(self,request):

        serializer=AuditLogSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class AuditLogDetailAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,pk):

        log=get_object_or_404(AuditLog,pk=pk)
        serializer=AuditLogSerializer(log)
        return Response(serializer.data)
    

    def put(self,request,pk):
       

        log=get_object_or_404(AuditLog,pk=pk)
        serializer=AuditLogSerializer(log,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,pk):

        log=get_object_or_404(AuditLog,pk=pk)
        log.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    

"""


{
  "contract": 1, 
  "action_type": "Created",
  "description": "A new contract has been created.",  
  "timestamp": "2025-03-19T15:00:00Z" 
}



"""