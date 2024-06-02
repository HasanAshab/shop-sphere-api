from rest_framework.permissions import BasePermission
from http import HTTPMethod
from api.products.models import Product, Discount


class IsProductOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in (
            HTTPMethod.GET,
            HTTPMethod.HEAD,
            HTTPMethod.OPTIONS,
        ):
            return True

        if isinstance(obj, Product):
            return obj.seller == request.user

        if isinstance(obj, Discount):
            return obj.product.seller == request.user

        return False
