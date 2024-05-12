from django.urls import path
from .views import ProductsView, ProductView

urlpatterns = [
    path("products/", ProductsView.as_view(), name="products"),
    path("products/<int:pk>/", ProductView.as_view(), name="product"),
]