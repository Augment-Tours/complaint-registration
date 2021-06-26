from django.db import models
from api.models import Timestampable


class Word(Timestampable):
    # The definition that this word belongs to
    definition = models.CharField(max_length=500)

class Translation(Timestampable):
    # Contains a short hand of what language this translation is
    # Eg. AM, EN, FR, DE -> (Amharic, English, France, Deutsch)
    language = models.CharField(max_length=3)

    # The utf-8 character of this translation
    name = models.CharField(max_length=500)

    # The word this translation belongs to
    word = models.ForeignKey(Word,
                             related_name='word',
                             null=True,
                             on_delete=models.SET_NULL)