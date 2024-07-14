from rest_framework import permissions
from shop_sphere.products.models import Product, Discount


class IsProductOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if isinstance(obj, Product):
            return obj.seller == request.user

        if isinstance(obj, Discount):
            return obj.product.seller == request.user

        return False
