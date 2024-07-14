from django.urls import path
from .views import ProductsView, ProductView, ProductDiscountView

urlpatterns = [
    path("products/", ProductsView.as_view(), name="products"),
    path("products/<int:pk>/", ProductView.as_view(), name="product"),
    path(
        "products/<int:pk>/discount/",
        ProductDiscountView.as_view(),
        name="product_discount",
    ),
]
