from django import forms
from .models import Image

class AddPhoto(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddPhoto, self).__init__(*args, **kwargs)
        self.fields["author"].required = False
        self.fields["description"].required = False
        self.fields["title"].required = False

    class Meta:
        model = Image
        fields = ["image", "title", "description", "author"]
        widgets = {
            "author": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Title"}
            ),
            "image": forms.FileInput(
                attrs={"class": "form-control", "id": "image-input"},
            ),
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Title"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Description", "rows":3}
            )
        }