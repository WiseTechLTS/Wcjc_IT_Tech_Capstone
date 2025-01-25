from django.contrib import admin
from django.utils.html import format_html
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_id', 'title', 'status', 'view_ticket')

    def view_ticket(self, obj):
        return format_html(
            '<a href="{}" target="_blank">View Ticket</a>',
            f"/tickets/{obj.ticket_id}/"
        )
    view_ticket.short_description = "View Ticket"
