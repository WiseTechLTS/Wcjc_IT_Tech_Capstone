from rest_framework import generics
from .models import Department, HospitalTicket, ITTicket, TicketAttachment
from .serializers import (
    DepartmentSerializer,
    HospitalTicketSerializer,
    ITTicketSerializer,
    TicketAttachmentSerializer,
)

# -----------------------------------------------------------------------------
# Department Endpoints
# -----------------------------------------------------------------------------
class PrimaryDepartmentListView(generics.ListAPIView):
    """
    List primary departments (departments with no parent).
    """
    queryset = Department.objects.filter(parent__isnull=True)
    serializer_class = DepartmentSerializer


class SubDepartmentListView(generics.ListAPIView):
    """
    List sub-departments. Optionally filter by primary department via query parameter.
    """
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        primary_id = self.request.query_params.get('primary_department_id')
        if primary_id:
            return Department.objects.filter(parent_id=primary_id)
        return Department.objects.filter(parent__isnull=False)


# -----------------------------------------------------------------------------
# Hospital Ticket Endpoints
# -----------------------------------------------------------------------------
class HospitalTicketListCreateView(generics.ListCreateAPIView):
    """
    List and create HospitalTicket instances.
    """
    queryset = HospitalTicket.objects.all()
    serializer_class = HospitalTicketSerializer


class HospitalTicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific HospitalTicket.
    """
    queryset = HospitalTicket.objects.all()
    serializer_class = HospitalTicketSerializer


# -----------------------------------------------------------------------------
# IT Ticket Endpoints
# -----------------------------------------------------------------------------
class ITTicketListCreateView(generics.ListCreateAPIView):
    """
    List and create ITTicket instances.
    """
    queryset = ITTicket.objects.all()
    serializer_class = ITTicketSerializer


class ITTicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific ITTicket instance.
    """
    queryset = ITTicket.objects.all()
    serializer_class = ITTicketSerializer


# -----------------------------------------------------------------------------
# TicketAttachment Endpoints (Optional)
# -----------------------------------------------------------------------------
class TicketAttachmentListCreateView(generics.ListCreateAPIView):
    """
    List and create TicketAttachment instances.
    Note: Attachments are linked to an ITTicket.
    """
    queryset = TicketAttachment.objects.all()
    serializer_class = TicketAttachmentSerializer


class TicketAttachmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific TicketAttachment instance.
    """
    queryset = TicketAttachment.objects.all()
    serializer_class = TicketAttachmentSerializer
