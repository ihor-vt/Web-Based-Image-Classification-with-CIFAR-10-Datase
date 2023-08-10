import os
import tempfile
from django.shortcuts import render
from django.contrib import messages
from django.core.files.uploadedfile import SimpleUploadedFile

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

            prediction = predict_image(temp_file_path)

            # Read the content of the temporary file
            with open(temp_file_path, 'rb') as temp_file_content:
                content = temp_file_content.read()

            context = {
                'predicted_class': prediction,
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
            # print(f">>> UploadImageForm error: {form.errors}")
    else:
        form = UploadImageForm()
    return render(
        request,
        'imagerecognition/image_upload.html',
        {'form': form})
