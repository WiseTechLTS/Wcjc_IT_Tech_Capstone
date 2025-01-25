from django.urls import path
from .views import WorkOrderListCreateView, WorkOrderDetailView

urlpatterns = [
    path('', WorkOrderListCreateView.as_view(), name='work-order-list-create'),  # List and Create work orders
    path('<int:pk>/', WorkOrderDetailView.as_view(), name='work-order-detail'),  # Retrieve, Update, or Delete work order by ID
]
