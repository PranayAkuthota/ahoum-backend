from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    language = models.CharField(
        max_length=50,
        db_index=True
    )

    location = models.CharField(
        max_length=255,
        db_index=True
    )

    starts_at = models.DateTimeField(
        db_index=True
    )

    ends_at = models.DateTimeField()

    capacity = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="events"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


class Enrollment(models.Model):

    STATUS_CHOICES = [
        ("ENROLLED", "Enrolled"),
        ("CANCELLED", "Cancelled"),
    ]

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    seeker = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ENROLLED"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["event", "seeker"],
                name="unique_enrollment"
            )
        ]