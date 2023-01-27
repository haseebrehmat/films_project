from django.forms import ModelForm, TextInput
from ..models import Genre

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"
        exclude = ("is_deleted", "deleted_at")
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter name",
                    "required": True,
                }
            ),
        }