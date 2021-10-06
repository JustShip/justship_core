from django.conf import settings
from django.db import models

from justship.apps.core.models import TimeStampedModel


class Category(models.Model):
    name = models.CharField(verbose_name='Name', max_length=20)
    description = models.CharField(verbose_name='Description', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Resource(TimeStampedModel):
    url = models.URLField()
    category = models.ManyToManyField(
        Category,
        related_name='categories',
        verbose_name='Category',
        max_length=100,
        blank=True
    )
    image = models.URLField(verbose_name='Image', null=True, blank=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Resource'
        verbose_name_plural = 'Resources'
        ordering = ['created_at']
