from typing import List, Tuple

import numpy as np

from django.conf import settings
from PIL import Image as PILImage
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


model_path = settings.MODEL_PATH
model = load_model(model_path)
class_names = [
    'Airplane', 'Car', 'Bird', 'Cat', 'Deer',
    'Dog', 'Frog', 'Horse', 'Ship', 'Truck'
    ]
THRESHOLD = 10


def preprocess_image(image_path):
    """
    The preprocess_image function takes an image path as input and returns
    a processed version of the image.
    The processing steps are:
        1. Read the image from disk using PIL's Image module (Note that this
        means we need to install Pillow)
        2. Resize it to 32x32 pixels, since our model expects images of
        that size
        3. Convert it to an array using Keras' img_to_array utility function,
        which scales pixel values between 0 and 1
        (we originally loaded them as integers between 0 and 255). This is
        necessary because our model uses a sigmoid.

    :param image_path: Specify the path to an image
    :return: A numpy array of shape (32, 32, 3)
    """
    img = PILImage.open(image_path)
    img = img.resize((32, 32))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array


def predict_image(image_file: str) -> Tuple[
        str, float, str]:
    """
    The predict_image function takes an image file as input and
    returns the predicted class name, its percentage, and other
    classes that exceed the threshold.

    :param image_file: str: Pass in the file path of the image to be classified
    :param THRESHOLD: float: Threshold for considering other classes
    :return: A tuple of the predicted class name, the percentage, and a string
            with other classes that exceed the threshold
    """
    img_array = preprocess_image(image_file)

    predictions = model.predict(img_array)

    prediction_percentages = predictions[0] * 100

    class_percentages = {}
    for i, prob in enumerate(prediction_percentages):
        class_percentages[class_names[i]] = prob

    highest_class = max(class_percentages, key=class_percentages.get)
    highest_percent = class_percentages[highest_class]

    other_classes = [f'{k} - {round(v)}%' for k, v in class_percentages.items() if v > THRESHOLD and k != highest_class]

    the_most_predicted_class = f'{highest_class} - {round(highest_percent)}%'

    return the_most_predicted_class, other_classes
