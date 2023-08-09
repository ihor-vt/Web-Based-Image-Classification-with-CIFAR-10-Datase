from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth import login as login_user, authenticate, logout
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import (
    RegistrationForm,
    LoginForm,
)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = "users/password_reset.html"
    email_template_name = "users/password_reset_email.html"
    html_email_template_name = "users/password_reset_email.html"
    success_url = reverse_lazy("users:password_reset_done")
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = "users/password_reset_subject.txt"


def registration(request):
    """
    The registration function is responsible for handling
    the registration of new users.
    It does so by first checking if the request method is GET or POST.
    If it's GET, then we
    create a RegistrationForm object and render it to the user in a
    template called register.html,
    which will be created later on in this chapter. If it's POST, then
    we create another RegistrationForm object but this time with data from
    our request (request.POST). We check if that form is valid and if so we
    extract some data from our cleaned_data dictionary: email and password(s).
    We check whether both passwords match each other; otherwise,

    :param request: Get the request object
    :return: A form for registration
    """
    if request.method == "GET":
        form = RegistrationForm()
        return render(request, "users/register.html", {"form": form})

    elif request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email = cd["email"]
            password = cd["password1"]
            password2 = cd["password2"]

            if password != password2:
                messages.warning(request, "The passwords did not match")
                return render(
                    request, "users/register.html", {"form": form}
                )

            if User.objects.filter(email=email).exists():
                messages.warning(
                    request, "Such an account is already registered")
                return redirect("users:registration")

            hashed_password = make_password(password2)

            user = User.objects.create_user(
                email=email,
                password=hashed_password,
            )

            messages.success(request, "You have successfully registered")
            return redirect("users:login")

        else:
            return render(
                request, "users/register.html", {"form": form}
            )

    return render(request, "users/register.html", {"form": form})


def login(request):
    """
    The login function is responsible for logging in the user.
    It checks if the request method is GET or POST, and then it
    creates a form object.
    If the request method is GET, it returns an HTML page with a
    login form to enter data into.
    If the request method is POST, it validates data from this form
    and checks whether there are any errors in them. If there are no
    errors, then we check whether all fields have been filled out
    (email and password). If they have not been filled out completely - we
    display an error message on our site that says &quot;Fill in all
    fields&quot;. Then we try to authenticate

    :param request: Get the request object
    :return: A redirect to the main page if the user is authenticated,
    """
    if request.method == "GET":
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            if not email or not password:
                messages.warning(request, "Fill in all fields")
                return render(
                    request, "users/login.html", {"form": form}
                )
            print(f">>>: {form.data}")
            user = authenticate(request, email=email, password=password)
            print(f">>>>>> user: {user}")
            if user is not None:
                login_user(request, user)
                return redirect("mainpage:main_page")
            else:
                messages.warning(request, "Enter the correct data")
                return render(
                    request, "users/login.html", {"form": form}
                )
        else:
            return render(request, "users/login.html", {"form": form})


@login_required
def logoutuser(request):
    """
    The logoutuser function logs out the user and redirects them to
    the login page.

    :param request: Get the request object
    :return: The redirect function, which takes the user back to the login page
    """

    logout(request)
    return redirect("users:login")
