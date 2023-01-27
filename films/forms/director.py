from django import forms
from ..models import Director


class DirectorForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter name"}
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "email",
                "placeholder": "Enter Email",
            }
        )
    )

    class Meta:
        model = Director
        fields = "__all__"
        exclude = ("is_deleted", "deleted_at")
