from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from api.enums import STATUS
from api.test_utils import create_country
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

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Country.objects.count(), 1)
    
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

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Country.objects.count(), 0)
    
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

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Country.objects.count(), 0)
    
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

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Country.objects.count(), 1)
        self.assertEqual(Country.objects.first().status, STATUS.ACTIVE)
    
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

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Country.objects.count(), 1)
        self.assertEqual(Country.objects.first().timezone, None)
    
    
    
class EditCountryApiViewTests(APITestCase):
    def setUp(self) -> None:
        self.country = create_country("United Arab Emirates", "ETB", "ETH", "EAT", STATUS.ACTIVE)

    def post(self, body=None):
        url = reverse('locations:edit_country')
        return self.client.post(url, body, format="json")

    def test_edit_country_name(self):
        """
        Test successfully editing a countries name
        """
        data = {
            'country_id': self.country.id,
            'name': 'Ethiopia'
        }

        response = self.post(body=data)

        self.country.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.country.name, 'Ethiopia')
    
    def test_edit_country_symbol(self):
        """
        Test successfully editing a countries symbol
        """
        data = {
            'country_id': self.country.id,
            'symbol': 'UAE'
        }

        response = self.post(body=data)

        self.country.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.country.symbol, 'UAE')
    
    def test_edit_country_status(self):
        """
        Test successfully editing countries status
        """
        data = {
            'country_id': self.country.id,
            'status': STATUS.INACTIVE,
        }

        response = self.post(body=data)

        self.country.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.country.status, STATUS.INACTIVE)

class ListCountryApiViewTests(APITestCase):
    def setUp(self) -> None:
        self.country = create_country("United Arab Emirates", "ETB", "ETH", "EAT", STATUS.ACTIVE)

    def get(self):
        url = reverse('locations:list_country')
        return self.client.get(url)
    
    def test_successfully_list_countries(self):
        """
        Test successfully list countries
        """
        response = self.get()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['id'], self.country.id)

class SearchCountryApiViewTests(APITestCase):
    def setUp(self) -> None:
        self.country = create_country("United Arab Emirates", "ETB", "ETH", "EAT", STATUS.ACTIVE)

    def get(self, search_term):
        url = reverse('locations:search_country') + "?search_term=" + search_term
        return self.client.get(url)
    
    def test_successfully_search_countries_by_country_name(self):
        """
        Test successfully search countries by country name
        """
        response = self.get('United')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['id'], self.country.id)

    def test_successfully_search_countries_by_country_symbol(self):
        """
        Test successfully search countries by their country symbol
        """
        response = self.get('ETH')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['id'], self.country.id)