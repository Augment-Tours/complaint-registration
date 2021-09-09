from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from annoying.fields import AutoOneToOneField

from locations.models import Country
from api.models import Timestampable, Activatable
from model_utils import Choices

# Create your models here.
class ShilengaeUser(AbstractUser, Timestampable, Activatable):
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

    country = models.ForeignKey(Country, 
                                related_name='+',
                                null=True,
                                on_delete=models.SET_NULL)

    ROLE = Choices('SUPERADMIN', 'ADMIN', 'MODERATOR', 'GUEST', 'USER')
    type = models.CharField(choices=ROLE, max_length=50, default=ROLE.GUEST)

    class Meta:
        ordering = ['first_name']

class ShilengaeUserProfile(Timestampable):
    mobile_country_code = models.CharField(max_length=5, blank=True)
    mobile_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    registration_method = models.CharField(max_length=50, blank=True)
    company_name = models.CharField(max_length=50, blank=True)
    facebook_id = models.CharField(max_length=50, blank=True)
    operating_country = models.ForeignKey(Country,
                                          related_name='+',
                                          null=True,
                                          on_delete=models.SET_NULL)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    user = AutoOneToOneField(ShilengaeUser, related_name="profile", on_delete=models.CASCADE)
    online_status = models.BooleanField(default=False)
    business_user = models.BooleanField(default=False)
    
    verified_mobile = models.BooleanField(default=False)
    verified_email = models.BooleanField(default=False)
    verified_phone = models.BooleanField(default=False)
    verified_facebook = models.BooleanField(default=False)