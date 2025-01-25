from django.db import models

class Ticket(models.Model):
    """
    Represents a support ticket created by a user.
    """
    email = models.EmailField(
        help_text="The email address of the user creating the ticket."
    )
    subject = models.CharField(
        max_length=255,
        help_text="A short summary of the issue or request."
    )
    description = models.TextField(
        help_text="A detailed description of the issue or request."
    )
    token = models.CharField(
        max_length=255,
        unique=True,
        help_text="A unique JWT token for tracking the ticket."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="The timestamp when the ticket was created."
    )

    def __str__(self):
        return f"Ticket #{self.id} - {self.subject}"
