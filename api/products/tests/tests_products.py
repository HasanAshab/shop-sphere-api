from django.urls import reverse
from django.test import tag
from rest_framework.test import APITestCase
from rest_framework import status
from api.products.factories import ProductFactory


@tag("products")
class ProductsTestCase(APITestCase):
    def test_list_products(self):
        ProductFactory.create_batch(3)

        url = reverse("products")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_retrieve_product(self):
        product = ProductFactory()

        url = reverse("product", kwargs={"pk": product.pk})
        self.client.force_authenticate()
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], product.pk)
