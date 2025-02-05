from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.html import format_html
from .models import (
    Department,
    HospitalTicket,
    ITTicket,
    TicketAttachment,
)
class TicketAttachmentInline(GenericTabularInline):
    model = TicketAttachment
    extra = 1
    readonly_fields = ('file_preview',)
    fields = ('file', 'file_preview', 'uploaded_at')
    
    def file_preview(self, obj):
        if obj.file:
            file_url = obj.file.url
            if file_url.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                return format_html(
                    '<a href="{}" target="_blank">'
                    '<img src="{}" style="max-width:100px; max-height:100px;" /></a>',
                    file_url,
                    file_url
                )
            else:
                return format_html('<a href="{}" target="_blank">View Attachment</a>', file_url)
        return "No file"
    file_preview = "Attachment Preview"
    
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent')
    search_fields = ('name',)

@admin.register(HospitalTicket)
class HospitalTicketAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'patient_name',
        'primary_department',
        'sub_department',
        'priority',
        'created_at'
    )
    list_filter = ('primary_department', 'priority', 'created_at')
    search_fields = ('title', 'description', 'patient_name')

@admin.register(ITTicket)
class ITTicketAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'title', 
        'issue_category', 
        'device_info', 
        'created_at', 
        'file_thumbnail'
    )
    list_filter = ('created_at',)
    search_fields = ('title', 'description', 'issue_category')
    # inlines = [TicketAttachmentInline]  # Optional: include attachments inline if desired

    def file_thumbnail(self, obj):
        """
        Return an HTML thumbnail for the file if it's an image; otherwise, return a link.
        """
        if obj.file:
            file_url = obj.file.url
            if file_url.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                return format_html(
                    '<a href="{}" target="_blank">'
                    '<img src="{}" style="max-width:100px; max-height:100px;" /></a>',
                    file_url,
                    file_url
                )
            else:
                return format_html('<a href="{}" target="_blank">View File</a>', file_url)
        return "No File"
    file_thumbnail.short_description = "File Thumbnail"

@admin.register(TicketAttachment)
class TicketAttachmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_link', 'uploaded_at')
    readonly_fields = ('file_link',)

    def file_link(self, obj):
        """
        Return a clickable link to the uploaded file. For images, display a thumbnail.
        """
        if obj.file:
            if obj.file.url.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                return format_html(
                    '<a href="{}" target="_blank">'
                    '<img src="{}" style="max-width:100px; max-height:100px;" /></a>',
                    obj.file.url,
                    obj.file.url
                )
            return format_html('<a href="{}" target="_blank">View Attachment</a>', obj.file.url)
        return "No Attachment"
    file_link.short_description = "Attachment URL"

