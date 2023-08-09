from django import forms
from django.core.validators import EmailValidator

from .models import ContactsUs, SubscribeEmailNewsletter


class ContactForm(forms.ModelForm):
    """Represents a form for user contact information. It includes fields for
    the user's name, email, subject, and message. These fields have associated
    widgets that specify input types, classes, and placeholders. The form is
    linked to the ContactsUs model and includes the fields name, email,
    subject, and message."""
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
    """Represents a form for subscribing to an email newsletter. It includes
    a single field for the user's email address. The field has an email
    validator and is associated with a widget that specifies input classes,
    placeholder, and type. The form is linked to the SubscribeEmailNewsletter
    model and includes the email field."""
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
