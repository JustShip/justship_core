import string
import random
import datetime

from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from justship.apps.accounts import constants
from justship.apps.core.models import TimeStampedModel
from justship.apps.products import models as products_models


class User(AbstractUser):
    """
    User model
    """
    creator_type = models.CharField(
        verbose_name='Creator type',
        max_length=10,
        choices=constants.CREATOR_TYPE_CHOICES
    )

    # onboarding
    onboarding_completed = models.BooleanField(verbose_name='Is onboarding completed', default=False)

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

    # product relationship
    product_relation = models.ManyToManyField(products_models.Product, through='ProductRelationship')

    class Meta:
        ordering = ['username']

    def __str__(self) -> str:
        return self.get_full_name() or self.username

    def generate_temporal_code(self) -> str:
        """
        Generate a temporal code for email confirmation
        :return: string with random numbers
        """
        size = 10
        chars = string.ascii_uppercase + string.digits
        self.temporal_code = ''.join(random.choice(chars) for _ in range(size))
        return self.temporal_code


class Follow(TimeStampedModel):
    """
    Model for following user
    """
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed')

    @admin.display(
        boolean=True,
        ordering='created_at',
        description='follow recently?',
    )
    def is_recent(self) -> bool:
        """
        Return if the follow is recent or not
        :return:
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_at <= now

    def __str__(self) -> str:
        return '{} -> {}'.format(self.follower, self.followed)


class ProductRelationship(TimeStampedModel):
    """
    Model for representing relationships between users and products
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_follower')
    product = models.ForeignKey(products_models.Product, on_delete=models.CASCADE, related_name='followed_product')
    is_following = models.BooleanField()
    rights = models.CharField(max_length=30, choices=constants.RIGHTS_CHOICES, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'product'], name='Anti_duplicated_relation')
        ]

    def is_recent(self) -> bool:
        """
        Return if the follow is recent or not
        :return:
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_at <= now

    def __str__(self) -> str:
        return '{} -> {}'.format(self.user, self.product)
