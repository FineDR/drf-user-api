from drf_api.base import BaseListCreateAPIView, BaseRetrieveUpdateDestroyAPIView
from .models import Product
from .serializers import ProductSerializer

class ProductCreateListAPIView(BaseListCreateAPIView):
    model = Product
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.select_related('category', 'posted_by').prefetch_related('images')


class ProductRetrieveUpdateDestroyAPIView(BaseRetrieveUpdateDestroyAPIView):
    model = Product
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.select_related('category', 'posted_by').prefetch_related('images')