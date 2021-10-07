import string
import random
import datetime

from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from . import constants
from ..core.models import TimeStampedModel


class User(AbstractUser):

    creator_type = models.CharField(
        verbose_name='Creator type',
        max_length=10,
        choices=constants.CREATOR_TYPE_CHOICES
    )

    # onboarding
    onboarding_completed = models.BooleanField(default=False)

    # signup and confirmations
    temporal_code = models.CharField(max_length=10, null=True, blank=True)

    # badges
    verified = models.BooleanField(default=False)    
    patreon = models.BooleanField(default=False)
    team = models.BooleanField(default=False)

    # avatar
    avatar_file_id = models.CharField(max_length=255, null=True, blank=True)
    avatar_url = models.URLField(null=True, blank=True)
    avatar_thumbnail_url = models.URLField(null=True, blank=True)

    # cover
    cover_file_id = models.CharField(max_length=255, null=True, blank=True)
    cover_url = models.URLField(null=True, blank=True)
    cover_thumbnail_url = models.URLField(null=True, blank=True)

    follows = models.ManyToManyField('self', through='Follow')

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.get_full_name() or self.username
    
    def generate_temporal_code(self):
        size = 10
        chars=string.ascii_uppercase + string.digits
        self.temporal_code = ''.join(random.choice(chars) for _ in range(size))
        return self.temporal_code


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
