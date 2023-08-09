from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class CustomUserBackend(ModelBackend):
    """Custom user backend implementation for Django models
    that support custom authentication"""
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        print(f">> UserModel: {UserModel}")
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None
