from django.db import models

# Create your models here.
# tickets/models.py
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.urls import reverse

# -----------------------------------------------------------------------------
# Department Model (Hierarchical Structure)
# -----------------------------------------------------------------------------
class Department(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='children',
        help_text="Leave blank for primary departments."
    )

    class Meta:
        verbose_name_plural = "Departments"
        ordering = ['parent__name', 'name']

    def __str__(self):
        return f"{self.parent.name} > {self.name}" if self.parent else self.name

# -----------------------------------------------------------------------------
# Priority Level Choices
# -----------------------------------------------------------------------------
PRIORITY_LEVEL_CHOICES = [
    ('Low', 'Low — Minor or no immediate impact'),
    ('Medium', 'Medium — Manageable disruption'),
    ('High', 'High — Significant urgency'),
    ('Critical', 'Critical — Immediate attention required'),
]

# -----------------------------------------------------------------------------
# HospitalTicket Model with Department and Sub-Department Fields
# -----------------------------------------------------------------------------
class HospitalTicket(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    patient_name = models.CharField(max_length=255, blank=True, null=True)
    # Primary department: Only departments with no parent.
    primary_department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='primary_tickets',
        limit_choices_to={'parent__isnull': True},
        help_text="Select the primary department category."
    )
    # Sub-department: Only departments that are children.
    sub_department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sub_tickets',
        limit_choices_to={'parent__isnull': False},
        help_text="Select the sub-department (child of the primary department)."
    )
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_LEVEL_CHOICES,
        default="Low",
        help_text="Set the urgency level for the ticket."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()
        if self.sub_department:
            if not self.primary_department:
                raise ValidationError("A primary department must be selected if a sub-department is provided.")
            if self.sub_department.parent != self.primary_department:
                raise ValidationError("The sub-department must be a child of the selected primary department.")

    def get_absolute_url(self):
        # If you wish to enable a public “view on site” link, define a corresponding URL.
        return reverse('hospital-ticket-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"HospitalTicket: {self.title}"

# -----------------------------------------------------------------------------
# ITTicket Model (Standard IT Tickets)
# -----------------------------------------------------------------------------
class ITTicket(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    device_info = models.CharField(max_length=255, blank=True, null=True)
    issue_category = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('it-ticket-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"ITTicket: {self.title}"

# -----------------------------------------------------------------------------
# TicketAttachment Model (For File and Image Previews)
# -----------------------------------------------------------------------------
class TicketAttachment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    ticket = GenericForeignKey('content_type', 'object_id')
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment: {self.file.name}"


"""
--------------------------------------------------------------------------------
Example Departments & Sub-Departments:

Primary Departments (parent is NULL):
  - Medical
  - Administrative
  - Support

Sub-Departments:
  Under Medical:
    - ED (Emergency Department)
    - OPD (Outpatient Department)
    - Inpatient
    - Surgery (Operating Theatres)
    - ICU (Intensive Care Unit)
    - Pediatrics
    - OB-GYN (Obstetrics and Gynecology)
    - Cardiology
    - Oncology
    - Orthopedics
    - Neurology
    - Psychiatry
    - Dermatology
    - Radiology
    - Pathology

  Under Administrative:
    - Admissions
    - Billing
    - HR
    - MedicalRecords
    - QualityAssurance
    - PublicRelations

  Under Support:
    - Pharmacy
    - Laboratory
    - Biomedical
    - Housekeeping
    - Catering
    - Security
    - IT
    - Transport

Populate these records via the admin interface or fixtures.
"""
