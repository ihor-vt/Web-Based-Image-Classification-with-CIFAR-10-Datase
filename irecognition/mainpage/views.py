from django.shortcuts import render, redirect
from django.contrib import messages as ms
from django.utils import timezone
from django.core.mail import send_mail

from irecognition import settings
from .forms import ContactForm, SubscribeEmailNewsletterForm
from .tasks import contacts_us
from .messages_for_visiters import thank_message, subscribe_message
from .models import Image, Statistics, Model


def main_page(request):
    statistics = Statistics.objects.first()
    hours_passed = Statistics.hours_passed_since_default_date()

    context = {
        "contact_form": ContactForm(),
        "subscribe_form": SubscribeEmailNewsletterForm,
        "statistics": statistics,
        "hours_passed": hours_passed,
    }
    return render(request, 'mainpage/main.html', context=context)


def contacts(request):
    """
    The contacts function is a view that handles the contacts page.
    It renders the contact form and sends an email to the user with
    a thank you message.

    :param request: Get the request object
    :return: The contacts page with a form to send messages
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            form.save()
            subject, messages = thank_message(name)
            send_mail(subject, messages, settings.EMAIL_HOST_USER, [email])
            ms.success(
                request, "Your message has been received. Thank you!"
            )
            return redirect("mainpage:main_page")
    else:
        form = ContactForm()

    return redirect("mainpage:main_page")


def subscribe_newsletter(request):
    """
    The subscribe_newsletter function is called when a user submits
    the newsletter subscription form. It takes in the request object, and if
    it's a POST request, it creates an instance of SubscribeEmailNewsletterForm
    with the data from that POST request. If that form is valid (i.e., all
    fields are filled out correctly), then we save its email field to our
    database and send an email to ourselves notifying us of this new
    subscriber.

    :param request: Get the data from the form
    :return: A redirect to the previous page
    """
    if request.method == "POST":
        form = SubscribeEmailNewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            form.save()
            subject, message = subscribe_message(email)
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
    return redirect("mainpage:main_page")
