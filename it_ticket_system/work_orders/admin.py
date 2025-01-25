from django.contrib import admin
from django.utils.html import format_html
from .models import WorkOrder

@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'technician_signature', 'view_work_order')

    def view_work_order(self, obj):
        return format_html(
            '<a href="{}" target="_blank">View Work Order</a>',
            f"/work-orders/detail/{obj.pk}/"
        )
    view_work_order.short_description = "View Work Order"
