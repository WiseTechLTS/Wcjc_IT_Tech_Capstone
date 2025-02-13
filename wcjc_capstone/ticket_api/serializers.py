# serializers.py

from rest_framework import serializers
from .models import ParentDepartment, SubDepartment, Ticket, HospitalTicket

class ParentDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentDepartment
        fields = '__all__'


class SubDepartmentSerializer(serializers.ModelSerializer):
    # Include the parent department details in read-only mode.
    parent_department = ParentDepartmentSerializer(read_only=True)
    # Allow setting the parent department via its primary key.
    parent_department_id = serializers.PrimaryKeyRelatedField(
        queryset=ParentDepartment.objects.all(),
        source='parent_department',
        write_only=True
    )

    class Meta:
        model = SubDepartment
        fields = ['id', 'name', 'priority', 'parent_department', 'parent_department_id']


class TicketSerializer(serializers.ModelSerializer):
    # Include the sub-department details in read-only mode.
    sub_department = SubDepartmentSerializer(read_only=True)
    # Allow setting the sub-department via its primary key.
    sub_department_id = serializers.PrimaryKeyRelatedField(
        queryset=SubDepartment.objects.all(),
        source='sub_department',
        write_only=True
    )

    class Meta:
        model = Ticket
        fields = [
            'id', 'subject', 'description', 'status',
            'created_at', 'updated_at', 'sub_department', 'sub_department_id'
        ]


class HospitalTicketSerializer(serializers.ModelSerializer):
    # Include the ticket details in read-only mode.
    ticket = TicketSerializer(read_only=True)
    # Allow setting the ticket via its primary key.
    ticket_id = serializers.PrimaryKeyRelatedField(
        queryset=Ticket.objects.all(),
        source='ticket',
        write_only=True
    )

    class Meta:
        model = HospitalTicket
        fields = ['ticket', 'ticket_id', 'patient_id', 'room_number', 'additional_info']
