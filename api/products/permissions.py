from rest_framework.permissions import BasePermission
from http import HTTPMethod


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in (
            HTTPMethod.GET,
            HTTPMethod.HEAD,
            HTTPMethod.OPTIONS,
        ):
            return True

        return obj.seller == request.user
