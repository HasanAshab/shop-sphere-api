import factory
from .models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    seller = factory.SubFactory("shop_sphere.users.factories.UserFactory")
    category = factory.SubFactory(
        "shop_sphere.category_api.factories.CategoryFactory"
    )
    title = factory.Faker("sentence")
    description = factory.Faker("paragraph")
    price = factory.Faker("random_int", min=1)
    quantity = factory.Faker("random_int", min=1, max=100)

    class Meta:
        model = Product
