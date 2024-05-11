from django.urls import path
from .views import CategoriesView


urlpatterns = [
    path(
        "categories/",
        CategoriesView.as_view(),
        name="categories",
    ),
]
