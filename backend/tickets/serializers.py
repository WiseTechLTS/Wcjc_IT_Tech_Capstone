from rest_framework import serializers
from .models import Department, HospitalTicket, ITTicket, TicketAttachment

class DepartmentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Department model. This model captures both primary (parentless)
    and sub-departments (children) in a hierarchical structure.
    """
    class Meta:
        model = Department
        fields = ['id', 'name', 'parent']


class HospitalTicketSerializer(serializers.ModelSerializer):
    """
    Serializer for HospitalTicket, representing the unified hospital trouble ticket.
    The serializer handles both the primary_department (parent department) and the
    sub_department (child department) fields using nested representations for clarity.
    """
    primary_department = DepartmentSerializer(read_only=True)
    primary_department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.filter(parent__isnull=True),
        write_only=True,
        source='primary_department',
        help_text="Select the primary department (must have no parent)."
    )
    sub_department = DepartmentSerializer(read_only=True)
    sub_department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.filter(parent__isnull=False),
        write_only=True,
        source='sub_department',
        help_text="Select the sub-department (must be a child of the selected primary department)."
    )

    class Meta:
        model = HospitalTicket
        fields = [
            'id',
            'title',
            'description',
            'patient_name',
            'primary_department',
            'primary_department_id',
            'sub_department',
            'sub_department_id',
            'priority',
            'created_at',
            'updated_at',
        ]


class ITTicketSerializer(serializers.ModelSerializer):
    """
    Serializer for ITTicket, representing standard IT support requests.
    """
    class Meta:
        model = ITTicket
        fields = [
            'id',
            'title',
            'description',
            'device_info',
            'issue_category',
            'created_at',
            'updated_at',
        ]


class TicketAttachmentSerializer(serializers.ModelSerializer):
    """
    Serializer for TicketAttachment, which provides file or image attachments
    associated with a ticket via a GenericForeignKey.
    """
    class Meta:
        model = TicketAttachment
        fields = ['id', 'file', 'uploaded_at']
