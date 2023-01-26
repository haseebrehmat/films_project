from django.forms import ModelForm
from ..models import Genre

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"
        exclude = ("is_deleted", "deleted_at")