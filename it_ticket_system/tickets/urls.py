from django.urls import path
from . import views

urlpatterns = [
    path('create-ticket/', views.create_ticket, name='create_ticket'),
    path('tickets/', views.get_all_tickets, name='get_all_tickets'),
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('/', views.ticket_detail, name='ticket_detail'),
]
