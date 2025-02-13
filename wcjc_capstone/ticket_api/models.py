from django.db import models

# =============================================================================
# Constants for initial data population
# =============================================================================

# Parent departments for a hospital setting
PARENT_DEPARTMENTS = [
    {
        'name': 'Medical',
        'description': 'Clinical services including emergency, inpatient, and specialized care.'
    },
    {
        'name': 'Administrative',
        'description': 'Operational management, billing, human resources, and records.'
    },
    {
        'name': 'Support',
        'description': 'Services such as IT, security, facility maintenance, and more.'
    }
]

# Sub-departments with realistic priority levels within each parent department.
# The lower the number, the higher the operational priority.
SUB_DEPARTMENT_PAIRS = {
    'Medical': [
        ('ED', 1),            # Emergency Department
        ('ICU', 2),           # Intensive Care Unit
        ('Surgery', 3),       # Surgery
        ('Inpatient', 4),     # Inpatient Services
        ('Cardiology', 5),    # Cardiology
        ('Oncology', 6),      # Oncology
        ('Neurology', 7),     # Neurology
        ('OB-GYN', 8),        # Obstetrics & Gynecology
        ('Pediatrics', 9),    # Pediatrics
        ('OPD', 10),          # Outpatient Department
        ('Orthopedics', 11),   # Orthopedics
        ('Radiology', 12),    # Radiology
        ('Pathology', 13),    # Pathology
        ('Psychiatry', 14),   # Psychiatry
        ('Dermatology', 15)   # Dermatology
    ],
    'Administrative': [
        ('Admissions', 1),       # Admissions
        ('Billing', 2),          # Billing
        ('MedicalRecords', 3),   # Medical Records
        ('QualityAssurance', 4), # Quality Assurance
        ('HR', 5),               # Human Resources
        ('PublicRelations', 6)   # Public Relations
    ],
    'Support': [
        ('Pharmacy', 1),      # Pharmacy
        ('Laboratory', 2),    # Laboratory
        ('IT', 3),            # IT Support
        ('Security', 4),      # Security
        ('Housekeeping', 5),  # Housekeeping
        ('Transport', 6),     # Transport
        ('Biomedical', 7),    # Biomedical Engineering/Maintenance
        ('Catering', 8)       # Catering
    ]
}

# =============================================================================
# Django Models
# =============================================================================

class ParentDepartment(models.Model):
    """
    Represents a high-level hospital department (e.g., Medical, Administrative, Support).
    No priority is assigned at this strategic level.
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Optional description of the department."
    )

    class Meta:
        verbose_name = "Parent Department"
        verbose_name_plural = "Parent Departments"
        ordering = ['name']  # Order alphabetically by name

    def __str__(self):
        return self.name


class SubDepartment(models.Model):
    """
    Represents an operational sub-department linked to a ParentDepartment.
    Each sub-department has an assigned priority level that reflects its operational importance.
    Lower numbers indicate higher priority.
    """
    name = models.CharField(max_length=255)
    parent_department = models.ForeignKey(
        ParentDepartment,
        on_delete=models.CASCADE,
        related_name='sub_departments'
    )
    priority = models.PositiveIntegerField(
        help_text="Lower numbers indicate higher operational priority within the parent department."
    )

    class Meta:
        verbose_name = "Sub Department"
        verbose_name_plural = "Sub Departments"
        ordering = ['parent_department', 'priority']
        unique_together = ('name', 'parent_department')

    def __str__(self):
        return f"{self.name} (Priority: {self.priority})"


class TicketStatus(models.TextChoices):
    """
    Defines the possible statuses for a ticket.
    """
    OPEN = 'open', 'Open'
    IN_PROGRESS = 'in_progress', 'In Progress'
    CLOSED = 'closed', 'Closed'


class Ticket(models.Model):
    """
    Represents a generic ticket for logging incidents, service requests, or issues
    within a particular sub-department in the hospital system.
    """
    subject = models.CharField(max_length=255)
    description = models.TextField()
    sub_department = models.ForeignKey(
        SubDepartment,
        on_delete=models.CASCADE,
        related_name='tickets'
    )
    status = models.CharField(
        max_length=20,
        choices=TicketStatus.choices,
        default=TicketStatus.OPEN,
        help_text="Current status of the ticket."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
        ordering = ['-created_at']  # Most recent tickets appear first

    def __str__(self):
        return f"{self.subject} ({self.get_status_display()})"


class HospitalTicket(models.Model):
    """
    Represents a hospital-specific ticket that extends the generic Ticket model with
    additional details such as patient ID, room number, and any other pertinent information.
    """
    ticket = models.OneToOneField(
        Ticket,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='hospital_ticket'
    )
    patient_id = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Identifier for the patient involved (if applicable)."
    )
    room_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Room number associated with the ticket (if applicable)."
    )
    additional_info = models.TextField(
        blank=True,
        null=True,
        help_text="Any additional hospital-specific information."
    )

    class Meta:
        verbose_name = "Hospital Ticket"
        verbose_name_plural = "Hospital Tickets"

    def __str__(self):
        return f"Hospital Ticket for {self.ticket.subject}"
