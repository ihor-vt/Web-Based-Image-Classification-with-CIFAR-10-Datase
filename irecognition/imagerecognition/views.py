from django.shortcuts import render


def upload_image(request):
    return render(request, 'imagerecognition/image_upload.html')
