from locations.models import Country, Region, City
from api.enums import STATUS

def create_country(name, currency, symbol, timezone, status):
    country = Country(name=name, currency=currency, symbol=symbol, timezone=timezone, status=status)
    country.save()

    return country

def create_region(name, symbol, status, country=None):
    region = Region(name=name, symbol=symbol, status=status)
    if country == None:
        country = create_country('test country', 'CUR', 'SYM', 'EAT', STATUS.ACTIVE)
        country.save()
        region.country = country
    region.save()

    return region

def create_city(name, symbol, status, region=None):
    city = City(name=name, symbol=symbol, status=status)
    if region == None:
        region = create_region('test region', 'TSR', STATUS.ACTIVE)
        region.save()
        city.region = region
    city.save()

    return city
    
    