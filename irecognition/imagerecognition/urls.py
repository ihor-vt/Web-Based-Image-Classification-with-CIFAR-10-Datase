from django.urls import path

from . import views

app_name = "images"

urlpatterns = [
    path("", views.upload_image, name="upload_image"),
    path("predicts/", views.upload_image_button, name="prediction_button"),
]
