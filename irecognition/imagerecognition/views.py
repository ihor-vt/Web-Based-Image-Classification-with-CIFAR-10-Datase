import os
import tempfile
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UploadImageForm
from .predict import predict_image
from mainpage.models import Statistics


def upload_image(request):
    """
    The upload_image function is responsible for handling the image upload
    form. It will save the uploaded image to a temporary file and then pass it
    to the predict_image function, which will return a prediction of what class
    the image belongs to. The prediction result is then rendered in
    an HTML page.

    :param request: Get the http request that was sent to this view
    :return: A prediction result page
    """
    if request.method == 'POST':

        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']

            # Create a temporary file to save the uploaded image
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(image.read())
                temp_file_path = temp_file.name

            the_most_predicted_class, other_classes = predict_image(
                temp_file_path)

            # Read the content of the temporary file
            with open(temp_file_path, 'rb') as temp_file_content:
                content = temp_file_content.read()

            context = {
                'the_most_predicted_class': the_most_predicted_class,
                'other_classes': other_classes,
                'uploaded_image': content,
            }

            # Clean up the temporary file
            os.remove(temp_file_path)
            Statistics.update_statistics()
            return render(
                request,
                'imagerecognition/prediction_result.html',
                context,
            )
        else:
            messages.warning(
                request,
                "The file you uploaded\
                was either not an image or a corrupted image."
                )
    else:
        form = UploadImageForm()
    return render(
        request,
        'imagerecognition/image_upload.html',
        {'form': form})


def upload_image_button(request):
    if request.method == 'POST':
        if 'true_button' in request.POST:
            Statistics.update_successful()
            messages.info(
                request,
                "Thank you, we will take your application into consideration."
                )
        elif 'false_button' in request.POST:
            Statistics.update_negative()
            messages.info(
                request,
                "Thank you, we will take your application into consideration."
                )
        return redirect("images:upload_image")

    form = UploadImageForm()
    return render(
        request,
        'imagerecognition/image_upload.html',
        {'form': form})
