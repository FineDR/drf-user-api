from rest_framework import status,permissions
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import Contract
from .serializers import ContractSerializer
from rest_framework.generics import get_object_or_404
from .permissions import IsBoss


class ContractListCreateAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):
        
        contracts=Contract.objects.all()
        serializer=ContractSerializer(contracts,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        self.check_permissions(request)

        serializer=ContractSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def check_permissions(self, request):
       
        if request.method == "POST" and not IsBoss().has_permission(request, self):
            self.permission_denied(request, message="Only bosses can create contracts.")



class ContractDetailAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,pk):

        contract=get_object_or_404(Contract,pk=pk)
        serializer=ContractSerializer(contract)
        return Response(serializer.data)
    

    def put(self,request,pk):
        self.check_permissions(request)

        contract=get_object_or_404(Contract,pk=pk)
        serializer=ContractSerializer(contract,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,pk):
        self.check_permissions(request)

        contract=get_object_or_404(Contract,pk=pk)
        contract.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def check_permissions(self, request):
       
        if request.method in ["PUT", "DELETE"] and not IsBoss().has_permission(request, self):
            self.permission_denied(request, message="Only bosses can update or delete contracts.")

