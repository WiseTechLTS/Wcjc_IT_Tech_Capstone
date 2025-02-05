from django.shortcuts import render

# Create your views here.
# tickets/views.py
from rest_framework import generics
from .models import Department, HospitalTicket, ITTicket
from .serializers import DepartmentSerializer, HospitalTicketSerializer, ITTicketSerializer

# Department endpoints
class PrimaryDepartmentListView(generics.ListAPIView):
    """
    Returns primary departments (those with no parent).
    """
    queryset = Department.objects.filter(parent__isnull=True)
    serializer_class = DepartmentSerializer

class SubDepartmentListView(generics.ListAPIView):
    """
    Returns sub-departments. Optionally filter by primary department using
    ?primary_department_id=<id>
    """
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        primary_id = self.request.query_params.get('primary_department_id')
        if primary_id:
            return Department.objects.filter(parent_id=primary_id)
        return Department.objects.filter(parent__isnull=False)

# Ticket endpoints
class HospitalTicketListCreateView(generics.ListCreateAPIView):
    queryset = HospitalTicket.objects.all()
    serializer_class = HospitalTicketSerializer

class HospitalTicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HospitalTicket.objects.all()
    serializer_class = HospitalTicketSerializer

class ITTicketListCreateView(generics.ListCreateAPIView):
    queryset = ITTicket.objects.all()
    serializer_class = ITTicketSerializer

class ITTicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ITTicket.objects.all()
    serializer_class = ITTicketSerializer
