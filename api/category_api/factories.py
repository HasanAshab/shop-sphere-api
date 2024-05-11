import factory
from categories.models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    slug = factory.Faker("slug")

    class Meta:
        model = Category
