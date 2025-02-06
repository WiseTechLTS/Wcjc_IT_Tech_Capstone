from rest_framework import serializers
from .models import HospitalTicket

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


class TicketAttachmentSerializer(serializers.ModelSerializer):
    # Return the absolute URL for the file.
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = TicketAttachment
        fields = ['id', 'file_url', 'uploaded_at']

    def get_file_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.file.url)
        return obj.file.url


class ITTicketSerializer(serializers.ModelSerializer):
    # Nest the attachment serializer to expose file URL information.
    attachments = TicketAttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = ITTicket
        fields = '__all__'
