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

    def test_successfully_update_by_editing_ancestry(self):
        """
        Test if you can de-attach a grand_child and attach it to L1 parent
        parent                              parent                  
           |                              /        \ 
        child_2                       child_2     child_3    
           |                          
        child_3                                
        """
        self.child_2.add_parent(self.parent)
        self.child_3.add_parent(self.child_2)

        data = {
            'parent': self.parent.id
        }

        response = self.post(self.child_3.id, data)

        self.child_3.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Root parent now has 2 children
        self.assertEqual(self.parent.children.count(), 2)
        # Child 3 should only have self.parent as an ancestor because it has been detached from child_2
        self.assertEqual(self.child_3.ancestors.count(), 1)
        # Child 3 should have root parent as it's parent
        self.assertEqual(self.child_3.parent, self.parent)
        # Child 2 should have 0 children
        self.assertEqual(self.child_2.children.count(), 0)

    def test_successfully_update_by_editing_ancestry_2(self):
        """
        Test if you can de-attach a child from root parent and attach it to child_2
              parent                        parent                                                
            /        \                        |                          
        child_2     child_3       ->        child_2                          
                                              |                          
                                            child_3                                
        """
        self.child_2.add_parent(self.parent)
        self.child_3.add_parent(self.parent)

        data = {
            'parent': self.child_2.id
        }

        response = self.post(self.child_3.id, data)

        self.child_3.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Root parent now has 1 child
        self.assertEqual(self.parent.children.count(), 1)
        # Child 3 should only have self.parent as an ancestor because it has been detached from child_2
        self.assertEqual(self.child_3.ancestors.count(), 2)
        # Child 3 should have root parent as it's parent
        self.assertEqual(self.child_3.parent, self.child_2)
        # Child 2 should have 0 children
        self.assertEqual(self.child_2.children.count(), 1)