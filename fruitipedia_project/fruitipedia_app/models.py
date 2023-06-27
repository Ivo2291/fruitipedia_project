from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def check_first_letter(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def check_if_all_letters(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")


class ProfileModel(models.Model):
    MAX_FIRST_NAME_LENGTH = 25
    MIN_FIRST_NAME_LENGTH = 2
    MAX_LAST_NAME_LENGTH = 35
    MIN_LAST_NAME_LENGTH = 1
    EMAIL_MAX_LENGTH = 40
    MAX_PASSWORD_LENGTH = 20
    MIN_PASSWORD_LENGTH = 8

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=[
            validators.MinLengthValidator(MIN_FIRST_NAME_LENGTH),
            check_first_letter,
        ]
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        validators=[
            validators.MinLengthValidator(MIN_LAST_NAME_LENGTH),
            check_first_letter,
        ]
    )

    email = models.EmailField(
        max_length=EMAIL_MAX_LENGTH,
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        validators=[
            validators.MinLengthValidator(MIN_PASSWORD_LENGTH),
        ]

    )

    image_URL = models.URLField(
        null=True,
        blank=True,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        default=18,
    )


class FruitModel(models.Model):
    MAX_NAME_LENGTH = 30
    MIN_NAME_LENGTH = 2

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=[
            validators.MinLengthValidator(MIN_NAME_LENGTH),
        ]
    )

    image_URL = models.URLField()

    description = models.TextField()

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('pk',)
