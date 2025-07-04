from drf_api.base import BaseListCreateAPIView, BaseRetrieveUpdateDestroyAPIView
from .serializers import CategorySerializer
from .models import Category

class CategoryListCreateAPIView(BaseListCreateAPIView):
    model = Category
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(BaseRetrieveUpdateDestroyAPIView):
    model = Category
    serializer_class = CategorySerializer