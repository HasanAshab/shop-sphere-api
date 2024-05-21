from rest_framework import serializers
from .models import Product
from api.category_api.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    attachments = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "price",
            "quantity",
            "category",
            "attachments",
        )
