from django.db import models

from justship.apps.core.models import Tag, Social
from justship.apps.products.constants import PRODUCT_STATE_CHOICES


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    state = models.CharField(max_length=10, default='building', choices=PRODUCT_STATE_CHOICES)

    tags = models.ManyToManyField(Tag)
    socials = models.ManyToManyField(Social)

    # logo
    logo_file_id = models.CharField(max_length=255, null=True, blank=True)
    logo_url = models.URLField(null=True, blank=True)
    logo_thumbnail_url = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)
