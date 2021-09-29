from django.db import models

from core.justship.core.models import TimeStampedModel


class EmailLog(TimeStampedModel):
    sender = models.EmailField()
    to = models.EmailField()
    subject = models.CharField(max_length=255)
    html = models.TextField()

    def __str__(self):
        return str(self.id)
