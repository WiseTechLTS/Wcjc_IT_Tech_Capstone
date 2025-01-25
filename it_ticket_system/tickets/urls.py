from django.urls import path
from . import views

urlpatterns = [
    path('create-ticket/', views.create_ticket, name='create_ticket'),
    path('tickets/', views.get_all_tickets, name='get_all_tickets'),
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('work-order/<uuid:unique_id>/', views.work_order_view, name='work_order'),
    path('work-orders/', views.work_order_list_view, name='work_order_list'),
]
