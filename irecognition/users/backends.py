from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class CustomUserBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        print(f">> UserModel: {UserModel}")
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        print(f">> User: {user}")
        print(f">>> user.check_password(password): {user.check_password(password)}")
        if user.check_password(password):
            return user
        return None
