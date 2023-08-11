from unittest.mock import patch

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

USER_MODEL = get_user_model()


@patch.object(USER_MODEL, "save")
def test_create_user_returns_new_user(user_model_save_mock):
    expected_user_data = {
        "email": "test_email@test.com",
        "password": "12345678"
    }
    user = USER_MODEL.objects.create_user(**expected_user_data)

    assert isinstance(user, USER_MODEL)
    assert user.email == expected_user_data["email"]
    assert check_password(expected_user_data["password"], user.password)
    assert user.is_active is True
    assert user.is_staff is False
    assert user.is_superuser is False
    assert user.username is None
    user_model_save_mock.assert_called_once()


def test_create_user_raises_error_when_email_field_is_None():
    with pytest.raises(ValueError) as error_proxy:
        USER_MODEL.objects.create_user(email=None)

    actual_error = error_proxy.value

    assert actual_error.args[0] == "The 'email' field must be set."


@patch.object(USER_MODEL, "save")
def test_create_user_skips_password_setting_when_not_provided(
        user_model_save_mock):
    expected_user_email = "test_email@test.com"
    user = USER_MODEL.objects.create_user(email=expected_user_email)

    assert isinstance(user, USER_MODEL)
    assert user.email == expected_user_email
    assert user.password is None
    user_model_save_mock.assert_called_once()


@patch.object(USER_MODEL, "save")
def test_create_super_user_returns_new_super_user(user_model_save_mock):
    expected_user_data = {
        "email": "test_email@test.com",
        "password": "12345678"
    }
    user = USER_MODEL.objects.create_superuser(**expected_user_data)

    assert isinstance(user, USER_MODEL)
    assert user.email == expected_user_data["email"]
    assert check_password(expected_user_data["password"], user.password)
    assert user.is_staff is True
    assert user.is_superuser is True
    assert user.is_active is True
    assert user.username is None

    user_model_save_mock.assert_called_once()


@pytest.mark.parametrize(
    "field_value,expected_error_message",
    [
        ({"is_staff": False}, "Superuser must have is_staff=True."),
        ({"is_superuser": False}, "Superuser must have is_superuser=True.")
    ]
)
def test_create_super_user_raises_error_when_super_user_field_is_None(
        field_value, expected_error_message):
    with pytest.raises(ValueError) as error_proxy:
        USER_MODEL.objects.create_superuser(
            email="test@test.com", password=12345678, **field_value)

    actual_error = error_proxy.value

    assert actual_error.args[0] == expected_error_message
