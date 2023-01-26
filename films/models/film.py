from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django_softdelete.models import SoftDeleteModel

from .abstract import TimeStamped
from .director import Director
from .genre import Genre


class Film(TimeStamped, SoftDeleteModel):
    title = models.CharField(max_length=200)
    length = models.PositiveIntegerField(blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    rating = models.FloatField(
        blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    genres = models.ManyToManyField(Genre, blank=True)
    director = models.ForeignKey(
        Director, blank=True, null=True, on_delete=models.CASCADE
    )

    def __str__(self):
        if self.year:
            return f"{self.title} ({self.year})"
        return self.title

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            if field.verbose_name != "genre"
            else (
                field.verbose_name,
                Genre.objects.get(pk=field.value_from_object(self)).name,
            )
            for field in self.__class__._meta.fields[1:]
        ]
