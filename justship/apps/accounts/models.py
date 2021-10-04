import datetime

from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from . import constants
from ..core.models import TimeStampedModel


class User(AbstractUser):
    creator_type = models.CharField(
        verbose_name='Tipo de Creador',
        max_length=10,
        choices=constants.CREATOR_TYPE_CHOICES
    )
    follows = models.ManyToManyField('self', through='Follow')

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.get_full_name() or self.username


class Follow(TimeStampedModel):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed')

    @admin.display(
        boolean=True,
        ordering='created_at',
        description='follow recently?',
    )
    def is_recent(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_at <= now

    def __str__(self):
        return '{} -> {}'.format(self.follower, self.followed)
