from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:ticket_id>/', views.create_work_order, name='create_work_order'),
    path('detail/<int:pk>/', views.work_order_detail, name='work_order_detail'),
    path('work-order/<uuid:unique_id>/', views.work_order_view, name='work_order'),
    path('work-orders/', views.work_order_view, name='work_order_list'),
]
