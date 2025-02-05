from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Department, HospitalTicket, ITTicket
from .serializers import (
    DepartmentSerializer,
    HospitalTicketSerializer,
    ITTicketSerializer,
)

class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provides a read-only endpoint for listing all departments.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class SubDepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provides a read-only endpoint for listing sub-departments.
    Sub-departments are Departments with a non-null parent.
    Supports filtering by primary department via the query parameter:
        ?primary_department_id=<primary_dept_id>
    """
    # Only departments that have a parent (i.e. sub-departments)
    queryset = Department.objects.filter(parent__isnull=False)
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        primary_department_id = self.request.query_params.get('primary_department_id')
        if primary_department_id:
            queryset = queryset.filter(parent_id=primary_department_id)
        return queryset


class HospitalTicketViewSet(viewsets.ModelViewSet):
    """
    Endpoints for creating and managing Hospital Tickets.
    """
    queryset = HospitalTicket.objects.all()
    serializer_class = HospitalTicketSerializer


class ITTicketViewSet(viewsets.ModelViewSet):
    """
    Endpoints for creating and managing IT Tickets.
    """
    queryset = ITTicket.objects.all()
    serializer_class = ITTicketSerializer
