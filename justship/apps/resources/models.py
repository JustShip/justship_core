from django.conf import settings
from django.db import models

from justship.apps.core.models import TimeStampedModel


class Category(models.Model):
    name = models.CharField(verbose_name='Name', max_length=20)
    description = models.CharField(verbose_name='Description', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Resource(TimeStampedModel):
    url = models.URLField(unique=True)
    title = models.CharField(verbose_name='Title', max_length=100)
    image = models.URLField(verbose_name='Image', null=True, blank=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categories = models.ManyToManyField(
        Category,
        related_name='categories',
        verbose_name='Category',
        max_length=100,
        blank=True
    )
    vote_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Resource'
        verbose_name_plural = 'Resources'
        ordering = ['created_at']


class Vote(TimeStampedModel):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Vote'
        verbose_name_plural = 'Votes'
        constraints = [
            models.UniqueConstraint(fields=['resource', 'voted_by'], name='unique_vote')
        ]
