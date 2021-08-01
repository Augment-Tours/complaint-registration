from locations.models import Country, Region, City
from users.models import ShilengaeUser
from forms.models import Category, Form, FormField, FormField
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

    if country == False:
        pass
    elif country and not isinstance(country, Country):
        country = create_country(country, "TSC", "TSS", "EAT", STATUS.ACTIVE)
        user.country = country
    elif not country:
        country = create_country("Test country", "TSC", "TSS", "EAT", STATUS.ACTIVE)
        user.country = country
    user.save()
    return user

def create_category(name, children = []):
    category = Category(name=name)
    category.save()

    for child in children:
        child.add_parent(category)
    
    return category

def create_form(name):
    form = Form(name=name)
    form.save()

    return form

def create_form_field(type, description, hint, label, position, form, data):
    field = FormField(
        type=type,
        description=description,
        hint=hint,
        label=label,
        position=position,
        form=form,
        data=data
    )
    field.save()

    return field

def create_user_and_login(obj, username, password, country=None):
    user = create_user(username, password, country)
    obj.client.force_login(user)
    return user