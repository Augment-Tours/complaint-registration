from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from api.enums import STATUS
from api.test_utils import create_user_and_login
from locations.models import Country, Region, City


class CreateCountryApiViewTests(APITestCase):
    def setUp(self) -> None:
        self.user = create_user_and_login(self, "test_username", "123456")

    def post(self, pk, body=None):
        url = reverse('users:update_user', kwargs={'pk': pk})
        return self.client.post(url, body, format="json")
    
    def test_successfully_edit_username(self):
        """
        Test if you can successfully edit username
        """
        response = self.post(self.user.id, {'username': 'new_username'})

        self.user.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user.username, 'new_username')