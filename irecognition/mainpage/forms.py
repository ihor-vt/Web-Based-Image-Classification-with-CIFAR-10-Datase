from django import forms
from django.core.validators import EmailValidator

from .models import ContactsUs, SubscribeEmailNewsletter


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'name': 'name',
                'class': 'form-control',
                'placeholder': 'Your Name'}))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'type': 'email',
                'name': 'email',
                'class': 'form-control',
                'placeholder': 'Your Email'}))
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'name': 'subject',
                'class': 'form-control',
                'placeholder': 'Subject'}))
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'name': 'message',
                'class': 'form-control',
                'placeholder': 'Message', 'rows': 6}))

    class Meta:
        model = ContactsUs
        fields = ['name', 'email', 'subject', 'message']


class SubscribeEmailNewsletterForm(forms.ModelForm):
    email = forms.EmailField(
        validators=[EmailValidator()],
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "aria-describedby": "button-addon1",
                "name": "email",
                "type": "text",
                "placeholder": "Enter your email address",
            }
        ),
    )

    class Meta:
        model = SubscribeEmailNewsletter
        fields = ["email"]
