from locations.models import Country

def create_country(name, currency, symbol, timezone, status):
    country = Country(name=name, currency=currency, symbol=symbol, timezone=timezone, status=status)
    country.save()

    return country