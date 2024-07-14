from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from .models import Product, Discount
from .permissions import IsProductOwnerOrReadOnly
from .serializers import (
    ProductListSerializer,
    ProductSerializer,
    DiscountSerializer,
)


class ProductsView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProductListSerializer
    queryset = Product.objects.prefetch_related("category").all()


class ProductView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsProductOwnerOrReadOnly)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDiscountView(RetrieveUpdateDestroyAPIView):
    lookup_field = "product__pk"
    lookup_url_kwarg = "pk"
    permission_classes = (IsAuthenticated, IsProductOwnerOrReadOnly)
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()
