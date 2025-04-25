from rest_framework import status,permissions
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import Assets
from .serializers import AssetSerializer
from rest_framework.generics import get_object_or_404
from .permissions import IsBoss


class AssetsListCreateAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):
        
        assets=Assets.objects.all()
        serializer=AssetSerializer(assets,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        self.check_permissions(request)

        serializer=AssetSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def check_permissions(self, request):
       
        if request.method == "POST" and not IsBoss().has_permission(request, self):
            self.permission_denied(request, message="Only bosses can create assets.")



class AssetsDetailAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,pk):

        asset=get_object_or_404(Assets,pk=pk)
        serializer=AssetSerializer(asset)
        return Response(serializer.data)
    

    def put(self,request,pk):
        self.check_permissions(request)

        Asset=get_object_or_404(Assets,pk=pk)
        serializer=AssetSerializer(Asset,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,pk):
        self.check_permissions(request)

        Asset=get_object_or_404(Assets,pk=pk)
        Asset.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def check_permissions(self, request):
       
        if request.method in ["PUT", "DELETE"] and not IsBoss().has_permission(request, self):
            self.permission_denied(request, message="Only bosses can update or delete assets.")






"""
{
    "contract": 1, 
    "name": "New Asset Name",
    "plate_number": "XYZ1234",
    "description": "Description of the asset.",
    "status": "Available"
}

"""