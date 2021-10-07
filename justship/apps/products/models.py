from django.db import models

from justship.apps.core.models import Tag, Social


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    state = models.CharField(max_length=255, default='pending', choices=(
        ('building', 'Building'),
        ('operating', 'Operating'),
        ('closed', 'Closed')
    ))

    tags = models.ManyToManyField(Tag)
    socials = models.ManyToManyField(Social)

    # logo
    logo_file_id = models.CharField(max_length=255, null=True, blank=True)
    logo_url = models.URLField(null=True, blank=True)
    logo_thumbnail_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
