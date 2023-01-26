from django.forms import ModelForm
from ..models import Film

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = "__all__"
        exclude = ("is_deleted", "deleted_at")