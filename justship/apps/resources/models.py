from django.db import models


class Resource(models.Model):
    url = models.URLField()
    category = models.CharField(verbose_name='Category', max_length=100)
    image = models.URLField(verbose_name='Image', null=True, blank=True)
    description = models.TextField(verbose_name='Description')
