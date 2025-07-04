from drf_api.base import BaseListCreateAPIView,BaseRetrieveUpdateDestroyAPIView

from .serializers import MotocycleSerializer

from .models import MotocycleImage


class MotocycleListCreateAPIView(BaseListCreateAPIView):
    model = MotocycleImage
    serializer_class = MotocycleSerializer


class MotocycleRetrieveUpdateDestroyAPIView(BaseRetrieveUpdateDestroyAPIView):
    model = MotocycleImage
    serializer_class = MotocycleSerializer
  