from django.contrib import admin
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
from .models import Department, HospitalTicket, ITTicket, TicketAttachment

# -----------------------------------------------------------------------------
# Helper function to generate a thumbnail from an attachment.
# -----------------------------------------------------------------------------
def generate_thumbnail(attachment):
    """
    Returns an HTML snippet for the attachment thumbnail.
    For image files, display a thumbnail; for others, display a text link.
    """
    if attachment and attachment.file and attachment.file.url.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        return mark_safe(
            f'<div style="display:inline-block; margin:2px; max-width: 100px; max-height: 100px; border: 1px solid #ddd; '
            f'border-radius: 8px; overflow:hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">'
            f'<a href="{attachment.file.url}" target="_blank">'
            f'<img src="{attachment.file.url}" style="width:100%; height:auto;" alt="Thumbnail" /></a></div>'
        )
    elif attachment and attachment.file:
        return mark_safe(
            f'<div style="display:inline-block; margin:2px;">'
            f'<a href="{attachment.file.url}" target="_blank">View File</a></div>'
        )
    return ""

def generate_all_thumbnails(it_ticket):
    """
    Retrieve all attachments for a given ITTicket and return a concatenated
    HTML snippet of their thumbnails.
    """
    attachments = it_ticket.attachments.all()
    if attachments.exists():
        html = "".join([generate_thumbnail(att) for att in attachments])
        return mark_safe(html)
    return "No Attachment"


# -----------------------------------------------------------------------------
# Inline for TicketAttachment (for attaching files to IT tickets)
# -----------------------------------------------------------------------------
class TicketAttachmentInline(admin.TabularInline):
    model = TicketAttachment
    extra = 1
    readonly_fields = ('file_thumbnail',)
    fields = ('file', 'file_thumbnail')

    def file_thumbnail(self, obj):
        return generate_thumbnail(obj)
    file_thumbnail.short_description = "Thumbnail Preview"


# -----------------------------------------------------------------------------
# Department Admin
# -----------------------------------------------------------------------------
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent')
    search_fields = ('name',)
    view_on_site = False


# -----------------------------------------------------------------------------
# HospitalTicket Admin
# -----------------------------------------------------------------------------
@admin.register(HospitalTicket)
class HospitalTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'employee_name', 'primary_department', 'sub_department', 'priority', 'created_at')
    list_filter = ('primary_department', 'sub_department', 'priority', 'created_at')
    search_fields = ('title', 'employee_name', 'description')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('title', 'description')}),
        ('Patient & Department Details', {'fields': ('employee_name', 'primary_department', 'sub_department', 'priority')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    view_on_site = False


# -----------------------------------------------------------------------------
# ITTicket Admin
# -----------------------------------------------------------------------------
@admin.register(ITTicket)
class ITTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'device_info', 'issue_category', 'created_at', 'attachment_thumbnails')
    list_filter = ('created_at',)
    search_fields = ('title', 'description', 'device_info', 'issue_category')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('title', 'description')}),
        ('Device & Issue Information', {'fields': ('device_info', 'issue_category')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    inlines = [TicketAttachmentInline]
    view_on_site = False

    def attachment_thumbnails(self, obj):
        # Generate thumbnails for all attachments linked to the ITTicket.
        return generate_all_thumbnails(obj)
    attachment_thumbnails.short_description = "Attachment Thumbnails"

    def response_add(self, request, obj, post_url_continue=None):
        # After adding an ITTicket, redirect back to the change list.
        return HttpResponseRedirect("../")


# -----------------------------------------------------------------------------
# TicketAttachment Admin
# -----------------------------------------------------------------------------
@admin.register(TicketAttachment)
class TicketAttachmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_preview', 'uploaded_at', 'it_ticket')
    list_filter = ('uploaded_at',)
    search_fields = ('file',)
    readonly_fields = ('file_preview',)
    view_on_site = False

    def file_preview(self, obj):
        return generate_thumbnail(obj) or "No Attachment"
    file_preview.short_description = "File Preview"


# -----------------------------------------------------------------------------
# Admin Site Customization
# -----------------------------------------------------------------------------
admin.site.site_header = "Epic Ticketing System Administration"
admin.site.site_title = "Epic Admin Portal"
admin.site.index_title = "Welcome to the Epic Ticket Administration Dashboard"
