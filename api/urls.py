from django.urls import path, include


urlpatterns = [
    path(
        "api/",
        include("api.docs.urls"),
    ),
    path(
        "api/",
        include("api.authentication.urls"),
    ),
    path(
        "api/",
        include("api.accounts.urls"),
    ),
    path(
        "api/",
        include("api.category_api.urls"),
    ),
    path(
        "api/",
        include("api.products.urls"),
    ),
]
