from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    """Custom user model manager with 'email' as a main
    field for authentication purposes."""

    def create_user(
            self,
            email: str,
            password: str = None,
            **extra_fields) -> "User":
        """Create and save a new user.

        User can be created without password to support passwordless
        authentication.

        Args:
            email (str): user email address
            password (str | None, optional): user password. Defaults to None.

        Raises:
            ValueError: in case if provided email value is None

        Returns:
            User: new user entity
        """
        if email is None:
            raise ValueError("The 'email' field must be set.")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)

        user.save()
        return user

    def create_superuser(
            self,
            email: str,
            password: str,
            **extra_fields) -> "User":
        """Create and save a new super user.

        Args:
            email (str): superuser email address
            password (str): superuser password

        Raises:
            ValueError: in case if provided 'is_staff' value is None
            ValueError: in case if provided 'is_superuser' value is None

        Returns:
            User: new superuser entity
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Model representing User object.

    User model has email field set as username field. Also model has
    password field
    set as nullable to provide passwordless authentication. This
    field is present
    only to create superuser and have easy access to admin panel.
    """

    username = None
    last_name = None

    password = models.CharField(
        verbose_name="password", max_length=128, blank=False, null=True
    )
    email = models.EmailField(
        verbose_name="email address", unique=True, blank=False)

    is_active = models.BooleanField(
        verbose_name="active",
        default=True,
        help_text="Designates whether this user should be treated as active. "
        "Unselect this instead of deleting accounts.",
    )
    updated_at = models.DateTimeField(verbose_name="updated at", auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.email}: {self.username}"

    class Meta:
        db_table = "users"
        verbose_name = "user"

    def get_full_name(self):
        raise NotImplementedError(
            "This method is not implemented, since User model\
                has no 'last_name' field."
        )

    def mark_as_active(self):
        """Activate current user."""
        self.is_active = True
        self.save()

    def update_last_login(self):
        """Update user last login time."""
        self.last_login = timezone.now()
        self.save()
