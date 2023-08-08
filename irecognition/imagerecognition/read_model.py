from pathlib import Path

import numpy as np
import tensorflow as tf
from PIL import Image

from os.path import exists
import gdown

model_filename = "my-model-cifar-10_v2.h5"

if not exists(model_filename):
    url = 'https://drive.google.com/file/d/1OGS4ysC_lttI6SPOWp38n9KZ3zCKou0e/view?usp=sharing'
    output = model_filename
    gdown.download(url, output, quiet=False, fuzzy=True)

model = tf.keras.models.load_model(model_filename, compile=False)

classes = [
    'Airplane', 'Car', 'Bird', 'Cat', 'Deer',
    'Dog', 'Frog', 'Horse', 'Ship', 'Truck']


def resize_image(image_to_recognize):
    img = Image.open(image_to_recognize)
    img = img.resize((32, 32))
    img = img.convert("RGB")
    input_image = np.reshape(img, (-1, 32, 32, 3))
    return input_image


def predict_image(image):
    input_img = resize_image(image)
    predict_img = model.predict(input_img)
    print(predict_img)
    pred_class = classes[np.argmax(predict_img)]
    return pred_class


if __name__ == '__main__':
    print(predict_image(Path('/Users/mac/Documents/Cods/Try/Projects/Web-Based-Image-Classification-with-CIFAR-10-Datase/irecognition/media/images/tesla.jpeg')))
