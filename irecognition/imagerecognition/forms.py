from django import forms


class UploadImageForm(forms.Form):
    """It represents a form for uploading images"""
    image = forms.ImageField()
