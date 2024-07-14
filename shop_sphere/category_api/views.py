from rest_framework.generics import ListAPIView
from categories.models import Category
from .serializers import CategorySerializer


class CategoriesView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
