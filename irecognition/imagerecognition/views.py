from django.shortcuts import render
from django.conf import settings
import os
import tempfile
from PIL import Image as PILImage

from .forms import UploadImageForm
from .predict import predict_image
from mainpage.models import Statistics


def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']

            # Create a temporary file to save the uploaded image
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(image.read())
                temp_file_path = temp_file.name

            prediction = predict_image(temp_file_path)

            # Clean up the temporary file
            os.remove(temp_file_path)
            Statistics.update_statistics()
            return render(
                request,
                'imagerecognition/prediction_result.html',
                {'predicted_class': prediction}
            )
        else:
            print(f">>> form error: {form.errors}")
    else:
        form = UploadImageForm()
    return render(
        request,
        'imagerecognition/image_upload.html',
        {'form': form})
