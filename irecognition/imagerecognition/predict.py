import tensorflow as tf
from django.conf import settings
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import io
from PIL import Image as PILImage

model_path = settings.MODEL_PATH
model = load_model(model_path)
class_names = [
    'Airplane', 'Automobile', 'Bird', 'Cat', 'Deer',
    'Dog', 'Frog', 'Horse', 'Ship', 'Truck']


def preprocess_image(image_path):
    img = PILImage.open(image_path)
    img = img.resize((32, 32))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array


def predict_image(image_file):
    img_array = preprocess_image(image_file)

    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)
    predicted_class_name = class_names[predicted_class]

    return predicted_class_name
