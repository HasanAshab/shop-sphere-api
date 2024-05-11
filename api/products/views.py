from rest_framework.generics import ListCreateAPIView
from .models import Product
from .serializers import ProductSerializer


class ProductsView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


