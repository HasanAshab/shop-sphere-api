from django.urls import reverse
from django.test import tag
from rest_framework.test import APITestCase
from rest_framework import status
from shop_sphere.users.factories import UserFactory
from shop_sphere.products.factories import ProductFactory


@tag("products")
class ProductsTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_list_products(self):
        ProductFactory.create_batch(3)

        url = reverse("products")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_retrieve_product(self):
        product = ProductFactory()

        url = reverse("product", kwargs={"pk": product.pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], product.pk)
