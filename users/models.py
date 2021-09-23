from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.
from api.models import Timestampable, Activatable
from model_utils import Choices

class CRUser(AbstractUser, Timestampable, Activatable):
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

    email = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    TYPE = Choices('MEMBER', 'PRIVILEGED_MEMBER', 'MODERATOR')
    type = models.CharField(max_length=50, choices=TYPE, default=TYPE.MEMBER)


    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        ordering = ('-created_at',)