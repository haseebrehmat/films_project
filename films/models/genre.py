from django.db import models
from django_softdelete.models import SoftDeleteModel

from .abstract import TimeStamped


class Genre(TimeStamped, SoftDeleteModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
