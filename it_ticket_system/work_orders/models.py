from django.db import models
from tickets.models import Ticket  # Import the Ticket model for reference

class WorkOrder(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE, related_name='work_order')
    work_performed = models.TextField()
    parts_used = models.TextField(blank=True, null=True)
    technician_signature = models.CharField(max_length=255)
    customer_signature = models.CharField(max_length=255)
    on_site_hours = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    date_completed = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    stop_time = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Work Order for Ticket {self.ticket.ticket_id}"
