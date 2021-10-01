from django.contrib.auth.models import AbstractUser
from django.db import models

from . import constants


class User(AbstractUser):
    creator_type = models.CharField(
        verbose_name='Tipo de Creador',
        max_length=10,
        choices=constants.CREATOR_TYPE_CHOICES
    )

    def __str__(self):
        return self.get_full_name() or self.username
