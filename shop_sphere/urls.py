from django.urls import path, include


urlpatterns = [
    path(
        "api/",
        include("shop_sphere.docs.urls"),
    ),
    path(
        "api/",
        include("shop_sphere.authentication.urls"),
    ),
    path(
        "api/",
        include("shop_sphere.accounts.urls"),
    ),
    path(
        "api/",
        include("shop_sphere.category_api.urls"),
    ),
    path(
        "api/",
        include("shop_sphere.products.urls"),
    ),
]
