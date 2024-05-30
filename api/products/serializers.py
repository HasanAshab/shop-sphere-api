from rest_framework import serializers
from .models import Product
from api.category_api.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    thumbnail = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "price",
            "quantity",
            "category",
            "thumbnail",
        )
