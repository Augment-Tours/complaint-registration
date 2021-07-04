from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator


# Create your models here.
class ShilengaeUser(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        max_length=15,
        unique=True,
        help_text='Required. 15 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )

    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
