from django.test import tag
from django.urls import reverse
from rest_framework import status
from rest_framework.test import (
    APITestCase,
)
from shop_sphere.users.factories import (
    UserFactory,
)
from .factories import CategoryFactory


@tag("categories", "list_categories")
class CategoriesTestCase(APITestCase):
    url = reverse("categories")

    def setUp(self):
        self.user = UserFactory()

    def test_list_categories(self):
        CategoryFactory.create_batch(3)
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(len(response.data), 3)
