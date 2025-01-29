from django.db import models

class ITTicket(models.Model):
    customer_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=30)
    store_address = models.TextField()
    work_requested = models.TextField()
    store_contact_name = models.CharField(max_length=100)
    store_contact_phone = models.CharField(max_length=15)
    work_performed = models.TextField(blank=True,)  # Optional field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.account_number}"
