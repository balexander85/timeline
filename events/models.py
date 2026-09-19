from django.core.exceptions import ValidationError
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(
        blank=True,
        null=True,
        help_text="Leave blank for a single-day event.",
    )
    image = models.ImageField(upload_to="events/%Y/", blank=True)
    body = models.TextField(blank=True)

    class Meta:
        ordering = ["start_date"]

    def __str__(self):
        return self.title

    def clean(self):
        if self.end_date and self.end_date < self.start_date:
            raise ValidationError("End date cannot be before start date.")
