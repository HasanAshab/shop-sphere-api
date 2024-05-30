from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from .models import Product
from .serializers import ProductSerializer


from attachments.models import Attachment
from django.db.models import Prefetch


class ProductsView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProductSerializer
    queryset = Product.objects.prefetch_related(
        "category", Prefetch("attachments", queryset=Attachment.objects.all())
    ).all()


class ProductView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer
    queryset = Product.objects.none()

    def get_queryset(self):
        return self.request.user.products
