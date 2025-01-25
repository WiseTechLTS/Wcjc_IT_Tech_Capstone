from django.db import models
from django.template.loader import render_to_string
from pathlib import Path
import os

class WorkOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    store_address = models.TextField()
    work_requested = models.TextField()
    store_contact_name = models.CharField(max_length=100)
    store_contact_phone = models.CharField(max_length=15)
    work_performed = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Override save method to generate an HTML file for the work order.
        """
        super().save(*args, **kwargs)

        # Render the HTML template with work order data
        html_content = render_to_string('work_order_template.html', {'work_order': self})

        # Define directory for generated HTML files relative to STATIC_ROOT
        output_dir = Path('generated_work_orders')
        output_dir.mkdir(parents=True, exist_ok=True)

        # Define the file path for the HTML file
        file_path = output_dir / f'work_order_{self.id}.html'

        # Write the rendered content to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(html_content)

    def __str__(self):
        return f"{self.customer_name} ({self.account_number})"
