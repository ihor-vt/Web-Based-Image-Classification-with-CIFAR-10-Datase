from django import forms
from django.core.validators import EmailValidator


class RegistrationForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        validators=[EmailValidator()],
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "name": "email",
                "id": "email",
                "placeholder": "Email",
            }
        ),
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "type": "password",
                "name": "password",
                "id": "pswd",
                "placeholder": "Password",
            }
        ),
    )
    password2 = forms.CharField(
        label="Confirm password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "type": "password",
                "name": "password",
                "id": "pswd",
                "placeholder": "Confirm password",
            }
        ),
    )


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        validators=[EmailValidator()],
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "name": "email",
                "id": "email",
                "placeholder": "Email",
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "type": "password",
                "name": "password",
                "id": "pswd",
                "placeholder": "Password",
            }
        ),
    )
