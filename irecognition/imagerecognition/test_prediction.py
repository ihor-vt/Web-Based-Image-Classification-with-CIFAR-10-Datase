import pytest
from .predict import preprocess_image, predict_image


@pytest.fixture
def sample_image_path():
    return '/Users/mac/Documents/Cods/Try/Projects/Web-Based-Image-Classification-with-CIFAR-10-Datase/img/Image for testing service/Doc.jpeg'


def test_preprocess_image(sample_image_path):
    img_array = preprocess_image(sample_image_path)
    assert img_array.shape == (1, 32, 32, 3)
    assert img_array.max() <= 1.0
    assert img_array.min() >= 0.0


def test_predict_image(sample_image_path):
    predicted_class, other_classes = predict_image(sample_image_path)

    assert isinstance(predicted_class, str)
    assert isinstance(other_classes, list)

    assert predicted_class == "Dog - 100%"

    for other_class in other_classes:
        assert isinstance(other_class, str)
