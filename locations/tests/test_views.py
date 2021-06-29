from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from api.enums import STATUS
from locations.models import Country

class CreateCountryApiViewTests(APITestCase):
    def setUp(self) -> None:
        pass

    def post(self, body=None):
        url = reverse('locations:create_country')
        return self.client.post(url, body, format="json")
    
    def test_success(self):
        """
        Successfully create a country
        """
        data = {
            'currency': "ETB",
            'name': 'Ethiopia',
            'symbol': 'ETH',
            'timezone': 'East Africa Time',
            'status': STATUS.ACTIVE,
        }

        response = self.post(body=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Country.objects.count(), 1)
    
    def test_no_currency(self):
        """
        No currency input for creating a country should fail
        """
        data = {
            # 'currency': "ETB",
            'name': 'Ethiopia',
            'symbol': 'ETH',
            'timezone': 'East Africa Time',
            'status': STATUS.ACTIVE,
        }

        response = self.post(body=data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(Country.objects.count(), 0)
    
    def test_no_name(self):
        """
        No name input for creating a country should fail
        """
        data = {
            'currency': "ETB",
            # 'name': 'Ethiopia',
            'symbol': 'ETH',
            'timezone': 'East Africa Time',
            'status': STATUS.ACTIVE,
        }

        response = self.post(body=data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(Country.objects.count(), 0)
    
    def test_no_status(self):
        """
        No status input for creating a country should default to active
        """
        data = {
            'currency': "ETB",
            'name': 'Ethiopia',
            'symbol': 'ETH',
            'timezone': 'East Africa Time',
            # 'status': STATUS.ACTIVE,
        }

        response = self.post(body=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Country.objects.count(), 1)
        self.assertEquals(Country.objects.first().status, STATUS.ACTIVE)
    
    def test_no_timezone(self):
        """
        No timezone input for creating a country should default to null
        """
        data = {
            'currency': "ETB",
            'name': 'Ethiopia',
            'symbol': 'ETH',
            # 'timezone': 'East Africa Time',
            'status': STATUS.ACTIVE,
        }

        response = self.post(body=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Country.objects.count(), 1)
        self.assertEquals(Country.objects.first().timezone, None)
    
    
    