from locations.models import Country, Region, City
from users.models import ShilengaeUser
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
    

def create_user(username, password, country=None):
    user = ShilengaeUser(username=username)
    user.set_password(password)
    user.first_name = 'test_first_name'
    user.email = 'test@email.com'

    if country and not isinstance(country, Country):
        country = create_country(country, "TSC", "TSS", "EAT", STATUS.ACTIVE)
    elif not country:
        country = create_country("Test country", "TSC", "TSS", "EAT", STATUS.ACTIVE)

    user.country = country
    user.save()

    return user

def create_user_and_login(obj, username, password, country=None):
    user = create_user(username, password, country)
    obj.client.force_login(user)
    return user