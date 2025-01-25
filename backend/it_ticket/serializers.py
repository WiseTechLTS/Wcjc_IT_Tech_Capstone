from rest_framework import serializers
from .models import ITTicket

class ITTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITTicket
        fields = '__all__'
