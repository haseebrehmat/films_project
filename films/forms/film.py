from django.forms import (
    ModelForm,
    TextInput,
    NumberInput,
    Select,
    SelectMultiple,
    ChoiceField,
)
from ..models import Film


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = "__all__"
        exclude = ("is_deleted", "deleted_at")
        widgets = {
            "title": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Title",
                    "required": True,
                }
            ),
            "year": NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter year",
                    "required": True,
                }
            ),
            "rating": NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Rate between 0 - 10",
                    "required": True,
                    "min": 0,
                    "max": 10,
                }
            ),
            "length": NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "How long this movie?",
                    "required": True,
                }
            ),
            "director": Select(
                attrs={
                    "class": "form-control",
                    "required": True,
                }
            ),
            "genres": SelectMultiple(
                attrs={
                    "class": "form-control",
                    "required": True,
                }
            ),
        }
