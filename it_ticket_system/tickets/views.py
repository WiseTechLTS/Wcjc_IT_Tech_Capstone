from rest_framework import generics
from .models import WorkOrder
from .serializers import WorkOrderSerializer

class WorkOrderListCreateView(generics.ListCreateAPIView):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer

class WorkOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer
