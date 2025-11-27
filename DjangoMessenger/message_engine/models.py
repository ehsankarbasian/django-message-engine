from django.db import models
from django.conf import settings


class MessageEndpoint(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="message_endpoints",
    )

    identifier = models.CharField(
        max_length=255,
        help_text="A unique identifier for this endpoint (email, phone, chat_id, token, etc.)"
    )

    endpoint_type = models.CharField(
        max_length=100,
        help_text="Endpoint type (e.g. sms, email, telegram, push). "
    )

    verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    priority = models.PositiveIntegerField(
        default=100,
        help_text="Lower value means higher priority."
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        unique_together = ("user", "identifier", "endpoint_type")
        ordering = ["priority", "-verified", "-is_active", "endpoint_type"]

    def __str__(self):
        return f"{self.user} | {self.endpoint_type}: {self.identifier}"
