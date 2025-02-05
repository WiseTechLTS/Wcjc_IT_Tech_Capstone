# tickets/serializers.py
from rest_framework import serializers
from .models import Department, HospitalTicket, ITTicket

class DepartmentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ['id', 'name', 'parent', 'children']

    def get_children(self, obj):
        children = obj.children.all()
        return DepartmentSerializer(children, many=True).data

class HospitalTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalTicket
        fields = '__all__'

class ITTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITTicket
        fields = '__all__'
