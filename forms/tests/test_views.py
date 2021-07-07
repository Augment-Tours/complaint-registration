from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from api.enums import STATUS
from api.test_utils import create_user_and_login, create_category
from forms.models import Category


class UpdateCategoryApiViewTests(APITestCase):
    def setUp(self) -> None:
        self.user = create_user_and_login(self, "username", "password")
        self.parent: Category = create_category("Level 1")
        self.child_1: Category = create_category("Level 2 - 1")
        self.child_2: Category = create_category("Level 2 - 2")
        self.child_3: Category = create_category("Level 3")

    def post(self, pk, body=None):
        url = reverse('forms:category_update', kwargs={'pk': pk})

        return self.client.post(url, body, format="json")
    
    def test_successfully_update_category_name(self):
        """
        Successfully update a category name
        """
        data = {
            'name': "new name"
        }
        
        response = self.post(self.parent.id, body=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.parent.refresh_from_db()

        self.assertEqual(self.parent.name, "new name")
    
    def test_successfully_update_category_by_attaching_children_to_parents(self):
        data = {
            'parent': self.parent.id
        }

        response = self.post(self.child_1.id, data)

        self.child_1.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.child_1.parent, self.parent)
        self.assertEqual(self.child_1.ancestors.first(), self.parent)
        self.assertEqual(self.parent.descendants.first(), self.child_1)

    # TODO: Additional testing needed