from django.conf import settings
from django.db import models


class Resource(models.Model):
    url = models.URLField()
    category = models.CharField(verbose_name='Category', max_length=100, null=True, blank=True)
    image = models.URLField(verbose_name='Image', null=True, blank=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
