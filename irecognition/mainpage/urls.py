from django.urls import path

from . import views

app_name = "mainpage"

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path(
        "subscribe_newsletter/",
        views.subscribe_newsletter,
        name="subscribe_newsletter"
        ),
    path(
        'contact/',
        views.contacts,
        name='contact'
        ),
]
