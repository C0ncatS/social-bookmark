from django.core.files.base import ContentFile
from django.utils.text import slugify
from django import forms

import requests

from .models import Image


class ImageCreationForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["title", "url", "description"]
        widgets = {
            "url": forms.HiddenInput,
        }

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data["url"]
        name = slugify(image.title)
        extension = image_url.rsplit(".", 1)[1].lower()
        image_name = f"{name}.{extension}"
        # download image from the given URL
        response = requests.get(image_url)
        # save the image to storage
        # The save=False parameter is passed to prevent the object from being saved to the database
        image.image.save(
            image_name,
            ContentFile(response.content),
            save=False,
        )
        if commit:
            image.save()
        return image

    def clean_url(self):
        url = self.cleaned_data["url"]
        valid_extensions = ["jpg", "jpeg", "png"]
        extension = url.rsplit(".", 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError(
                "The given URL does not match valid image extensions."
            )
        return url
