from django.db import models

from api.models import Timestampable
from api.enums import STATUS

class Country(Timestampable):
    # Symbol of Currency
    currency = models.CharField(max_length=4)

    # Name of the Country (TODO: link to word)
    name = models.CharField(max_length=100)

    # Symbol of the country
    symbol = models.CharField(max_length=5)

    # The timezone symbol of the country
    timezone = models.CharField(max_length=50, blank=True, null=True)
    
    # The status of this country
    status = models.CharField(choices=STATUS, max_length=10, default=STATUS.ACTIVE)

class Region(Timestampable):
    # Name of the Region (TODO: link to word)
    name = models.CharField(max_length=100)

    # Symbol of the Region
    symbol = models.CharField(max_length=5)

    # The country this region belongs to
    country = models.ForeignKey(Country,
                                related_name='regions',
                                on_delete=models.SET_NULL,
                                null=True)

    # The status of this region
    status = models.CharField(choices=STATUS, max_length=10, default=STATUS.ACTIVE)


class City(Timestampable):
    # Name of the City (TODO: link to word)
    name = models.CharField(max_length=100)

    # Symbol of the Region
    symbol = models.CharField(max_length=5)

    # The region this city belongs to
    region = models.ForeignKey(Region,
                                related_name='cities',
                                on_delete=models.SET_NULL,
                                null=True)

    # The status of this city
    status = models.CharField(choices=STATUS, max_length=10, default=STATUS.ACTIVE)