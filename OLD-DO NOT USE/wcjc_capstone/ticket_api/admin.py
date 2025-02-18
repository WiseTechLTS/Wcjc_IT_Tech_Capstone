# ticket_api/admin.py

from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from django.db.models import Count
from django.db.models.functions import TruncHour
import json

from .models import ParentDepartment, SubDepartment, Ticket, HospitalTicket


class DashboardAdminSite(admin.AdminSite):
    """
    A custom admin site with an integrated dashboard.
    Designed with clarity and maintainability in mind.
    """
    site_header = "Hospital Management Dashboard"
    site_title = "Hospital Dashboard"
    index_title = "Welcome to the Hospital Data Dashboard"

    def get_urls(self):
        """Extend the default admin URLs with our custom dashboard view."""
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view), name="dashboard"),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        """
        Assemble the context for the dashboard:
          - Basic metrics: total counts of departments and tickets.
          - Timeline data: group tickets by creation hour.
        """
        # Aggregate key metrics
        total_parent_departments = ParentDepartment.objects.count()
        total_sub_departments = SubDepartment.objects.count()
        total_tickets = Ticket.objects.count()
        total_hospital_tickets = HospitalTicket.objects.count()

        # Create timeline data by grouping tickets by hour
        timeline_qs = Ticket.objects.annotate(
            hour=TruncHour('created_at')
        ).values('hour').annotate(
            count=Count('id')
        ).order_by('hour')

        timeline_data = {
            "labels": [entry["hour"].strftime("%Y-%m-%d %H:%M") for entry in timeline_qs],
            "counts": [entry["count"] for entry in timeline_qs],
        }

        context = self.each_context(request)
        context.update({
            "total_parent_departments": total_parent_departments,
            "total_sub_departments": total_sub_departments,
            "total_tickets": total_tickets,
            "total_hospital_tickets": total_hospital_tickets,
            "timeline_data": json.dumps(timeline_data),  # Pass as JSON string for JS consumption
        })
        return TemplateResponse(request, "admin/dashboard.html", context)


# Instantiate our custom admin site
dashboard_site = DashboardAdminSite(name='dashboard_admin')


# ModelAdmin registrations remain mostly standard
@admin.register(ParentDepartment)
class ParentDepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(SubDepartment)
class SubDepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_department', 'priority')
    list_filter = ('parent_department',)
    search_fields = ('name', 'parent_department__name')
    ordering = ('parent_department', 'priority')


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sub_department', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'sub_department')
    search_fields = ('subject', 'description', 'sub_department__name')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(HospitalTicket)
class HospitalTicketAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'patient_id', 'room_number')
    search_fields = ('ticket__subject', 'patient_id', 'room_number')
    ordering = ('ticket',)


# Also register models with the custom dashboard admin site
dashboard_site.register(ParentDepartment, ParentDepartmentAdmin)
dashboard_site.register(SubDepartment, SubDepartmentAdmin)
dashboard_site.register(Ticket, TicketAdmin)
dashboard_site.register(HospitalTicket, HospitalTicketAdmin)
