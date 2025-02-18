# tickets/urls.py
from django.urls import path
from .views import (
    PrimaryDepartmentListView,
    SubDepartmentListView,
    HospitalTicketListCreateView,
    HospitalTicketDetailView,
    ITTicketListCreateView,
    ITTicketDetailView,
)

urlpatterns = [
    # Department endpoints
    path('departments/primary/', PrimaryDepartmentListView.as_view(), name='primary-department-list'),
    path('departments/sub/', SubDepartmentListView.as_view(), name='sub-department-list'),

    # Hospital Tickets
    path('hospital-tickets/', HospitalTicketListCreateView.as_view(), name='hospital-ticket-list-create'),
    path('hospital-tickets/<int:pk>/', HospitalTicketDetailView.as_view(), name='hospital-ticket-detail'),

    # IT Tickets
    path('it-tickets/', ITTicketListCreateView.as_view(), name='it-ticket-list-create'),
    path('it-tickets/<int:pk>/', ITTicketDetailView.as_view(), name='it-ticket-detail'),
]
