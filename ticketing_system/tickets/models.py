from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

# Priority mapping based on sub-department
SUB_DEPARTMENT_PRIORITY_MAPPING = {
    "ED": "Critical",
    "ICU": "Critical",
    "Surgery": "High",
    "Inpatient": "High",
    "Cardiology": "High",
    "Neurology": "High",
    "Oncology": "Medium",
    "Pediatrics": "Medium",
    "Psychiatry": "Medium",
    "Radiology": "Medium",
    "Pathology": "Medium",
    "Admissions": "High",
    "Billing": "Medium",
    "HR": "Low",
    "MedicalRecords": "Medium",
    "QualityAssurance": "Low",
    "PublicRelations": "Low",
    "Pharmacy": "High",
    "Laboratory": "Medium",
    "Biomedical": "Medium",
    "Housekeeping": "Low",
    "Catering": "Low",
    "Security": "High",
    "IT": "High",
    "Transport": "Medium",
}

class HospitalTicket(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    patient_name = models.CharField(max_length=255, blank=True, null=True)
    primary_department = models.ForeignKey(
        'Department',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='primary_tickets',
        limit_choices_to={'parent__isnull': True},
        help_text="Select the primary department category."
    )
    sub_department = models.ForeignKey(
        'Department',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sub_tickets',
        limit_choices_to={'parent__isnull': False},
        help_text="Select the sub-department (child of the primary department)."
    )
    priority = models.CharField(
        max_length=10,
        choices=[
            ('Low', 'Low — Minor or no immediate impact'),
            ('Medium', 'Medium — Manageable disruption'),
            ('High', 'High — Significant urgency'),
            ('Critical', 'Critical — Immediate attention required'),
        ],
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

    def save(self, *args, **kwargs):
        """ Auto-assign priority based on the selected sub-department """
        if self.sub_department:
            self.priority = SUB_DEPARTMENT_PRIORITY_MAPPING.get(self.sub_department.name, "Low")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('hospital-ticket-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"HospitalTicket: {self.title}"
