"""
Django Models for IT Ticket System

This module defines the data structure for storing IT tickets in a database. It uses Django's ORM (Object-Relational Mapping)
to create tables and manage CRUD operations.

Classes:
- Ticket: Represents an IT ticket with user details, department, priority, status, timestamps, and optional attachments.

Fields:
- `ticket_id`: Unique UUID for each ticket.
- `name`: User's full name.
- `email`: User's email for correspondence.
- `phone`: Optional field for user's phone number.
- `address`: Optional field for user's physical address.
- `department`: Categorization of the ticket (IT, Medical, etc.).
- `sub_department`: Further classification within a department.
- `issue`: Description of the problem or request.
- `priority`: Urgency level (Low, Medium, High, Critical).
- `status`: Tracks the resolution process (Open, In Progress, Resolved, Closed).
- `screenshot`: Optional file upload field for evidence.
- `created_at`: Timestamp when the ticket was created.
- `updated_at`: Timestamp of the latest modification.

Django Features:
- Uses `UUIDField` for unique ticket IDs.
- Auto-updates timestamps with `auto_now_add` and `auto_now`.
- Provides human-readable string representation in `__str__`.
"""
from django.db import models
import uuid

class Ticket(models.Model):
    """Represents a support ticket in the IT ticketing system."""
    
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]

    DEPARTMENT_CHOICES = [
        ('IT (User Submission)', 'IT (User Submission)'),
        ('Medical', 'Medical'),
        ('Administrative', 'Administrative'),
        ('Support', 'Support'),
    ]

    ticket_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True,
        help_text="Automatically generated unique identifier for each ticket."
    )

    name = models.CharField(max_length=255, help_text="Full name of the ticket submitter.")
    email = models.EmailField(help_text="User's email address for ticket communication.")
    phone = models.CharField(max_length=20, blank=True, null=True, help_text="Optional user phone number.")
    address = models.TextField(blank=True, null=True, help_text="Optional user address.")

    department = models.CharField(
        max_length=50, choices=DEPARTMENT_CHOICES,
        help_text="Main department responsible for the ticket."
    )
    sub_department = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="Optional sub-category under the main department."
    )

    issue = models.TextField(help_text="Detailed description of the problem reported.")
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default='Medium',
        help_text="Priority level of the issue."
    )
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default='Open',
        help_text="Current state of the ticket."
    )

    screenshot = models.ImageField(
        upload_to='ticket_screenshots/', blank=True, null=True,
        help_text="Optional screenshot upload for visual reference."
    )

    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp of when the ticket was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp of last update.")

    def __str__(self):
        """
        Returns a human-readable representation of the ticket.
        Example: Ticket <UUID> - IT - Open
        """
        return f"Ticket {self.ticket_id} - {self.department} - {self.status}"
