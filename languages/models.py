from django.db import models

# Create your models here.
from django.db import models
from api.models import Timestampable


class Word(Timestampable):
    # The definition that this word belongs to
    definition = models.CharField(max_length=500)
    
    # The default value if the word is not to be found in the language pack
    default = models.CharField(max_length=200)