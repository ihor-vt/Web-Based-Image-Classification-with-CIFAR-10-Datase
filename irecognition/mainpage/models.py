from datetime import datetime, timedelta

from typing import Any
from django.db import models

from users.models import User


class UserImage(models.Manager):
    """: A custom manager for creating Image instances
    with additional statistics updates."""
    def create(self, count_successful=0, count_negative=0, **kwargs):
        user_mage = self.model(**kwargs)
        user_mage.save()

        stat = Statistics.objects.first()
        stat(
            total=stat.total + 1,
            count_successful=stat.count_successful + count_successful,
            count_negative=count_negative + count_negative,
        )

        return user_mage


class Image(models.Model):
    """Represents an image with an associated image file
    and a classification label."""
    image = models.ImageField(upload_to='images/')
    image_class = models.CharField(max_length=15, null=True)

    objects = UserImage()

    def __str__(self) -> str:
        return f"{self.image_class}"


class Model(models.Model):
    """Represents a model with a name field."""
    name = models.CharField(max_length=80, null=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Statistics(models.Model):
    """Stores statistics related to successful and negative image
    classifications, along with a default developer value. Provides
    methods to calculate hours passed since a default date and update
    statistics."""
    total = models.IntegerField(default=0)
    count_successful = models.IntegerField(default=0)
    count_negative = models.IntegerField(default=0)
    developer = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"Total: {self.total}"

    @staticmethod
    def hours_passed_since_default_date():
        default_datetime = datetime.strptime(
            "2023-08-08T00:00:00", "%Y-%m-%dT%H:%M:%S")
        current_datetime = datetime.now()
        hours_passed = (
            current_datetime - default_datetime).total_seconds() / 3600
        return hours_passed

    @staticmethod
    def update_statistics():
        stat = Statistics.objects.first()
        stat.total += 1
        stat.count_successful += 1
        stat.save()


class ContactsUs(models.Model):
    """Represents user contact information, including name,
    email, subject, message, and date of submission."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.email}: {self.subject}"


class SubscribeEmailNewsletter(models.Model):
    """Stores email addresses for newsletter subscription."""
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return f"{self.email}"
