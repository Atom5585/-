from django import forms
from .models import Advertisiment
from django.forms import ModelForm
class AdvertisimentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs["class"] = "form-control form-control-lg"
        self.fields["description"].widget.attrs["class"] = "form-control form-control-lg"
        self.fields["image"].widget.attrs["class"] = "form-control form-control-lg"
        self.fields["price"].widget.attrs["class"] = "form-control form-control-lg"
        self.fields["auction"].widget.attrs["class"] = "form-control form-control-lg"

        class Meta:
            model = Advertisiment
            fields = ["title", "description", "image", "price", "auction"]

        def clean_title(self):
            title = self.cleaned_data["title"]
            if title.startswish("?"):
                raise ValidationError("not ?")
            return title