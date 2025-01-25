from django.urls import path
from . import views

urlpatterns = [
    path('create-ticket/', views.create_ticket, name='create_ticket'),
    path('list-tickets/', views.list_tickets, name='list_tickets'),
]
