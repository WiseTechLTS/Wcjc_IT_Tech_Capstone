# views.py

from rest_framework import viewsets
from django.template.response import TemplateResponse
from .models import ParentDepartment, SubDepartment, Ticket, HospitalTicket
from .serializers import (
    ParentDepartmentSerializer,
    SubDepartmentSerializer,
    TicketSerializer,
    HospitalTicketSerializer,
)

class ParentDepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Parent Departments to be viewed or edited.
    """
    queryset = ParentDepartment.objects.all()
    serializer_class = ParentDepartmentSerializer


class SubDepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Sub-Departments to be viewed or edited.
    """
    queryset = SubDepartment.objects.all()
    serializer_class = SubDepartmentSerializer


class TicketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tickets to be viewed or edited.
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class HospitalTicketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Hospital Tickets to be viewed or edited.
    """
    queryset = HospitalTicket.objects.all()
    serializer_class = HospitalTicketSerializer

def dashboard_view(self, request):
    context = dict(
        self.each_context(request),
        total_parent_departments=ParentDepartment.objects.count(),
        total_sub_departments=SubDepartment.objects.count(),
        total_tickets=Ticket.objects.count(),
        total_hospital_tickets=HospitalTicket.objects.count(),
        recent_tickets=Ticket.objects.order_by('-created_at')[:10],
    )
    return TemplateResponse(request, "admin/dashboard.html", context)
