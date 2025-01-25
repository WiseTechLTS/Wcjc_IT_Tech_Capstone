from django.contrib import admin
from django.utils.html import format_html
from .models import WorkOrder

class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'account_number', 'created_at', 'view_html')

    def view_html(self, obj):
        """
        Provide a link to view the generated HTML file.
        """
        file_path = f'/generated_work_orders/work_order_{obj.id}.html'
        return format_html('<a href="{}" target="_blank">View HTML</a>', file_path)

    view_html.short_description = 'HTML Preview'

admin.site.register(WorkOrder, WorkOrderAdmin)
