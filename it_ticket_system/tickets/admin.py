from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'unique_id',
        'ticket_id',
        'email',
        'title',
        'status',
        'escalation_level',
        'created_at',
        'updated_at',
    )
    list_filter = ('status', 'escalation_level', 'created_at')
    search_fields = ('email', 'title', 'description', 'unique_id')
    ordering = ('-created_at',)

    fieldsets = (
        ("Ticket Information", {
            'fields': ('unique_id', 'email', 'ticket_id', 'title', 'description', 'attachment')
        }),
        ("Status and Escalation", {
            'fields': ('status', 'escalation_level')
        }),
        ("Timestamps", {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('unique_id', 'ticket_id', 'created_at', 'updated_at')

    def has_add_permission(self, request):
        """Disallow manual addition of tickets from admin panel."""
        return False

    def has_delete_permission(self, request, obj=None):
        """Allow ticket deletion only for superusers."""
        return request.user.is_superuser
