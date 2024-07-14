from rest_framework import serializers
from attachments.models import Attachment
from shop_sphere.common.serializers import TruncatedCharField
from shop_sphere.category_api.serializers import CategorySerializer
from .models import Product, Discount


class ProductAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = (
            "attachment_file",
            "created",
            "modified",
        )


class ProductListSerializer(serializers.ModelSerializer):
    title = TruncatedCharField(max_length=5)
    category = CategorySerializer(read_only=True)
    thumbnail = ProductAttachmentSerializer(read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "price",
            "quantity",
            "category",
            "thumbnail",
            "discount_price",
        )


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    attachments = ProductAttachmentSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "description",
            "price",
            "quantity",
            "category",
            "attachments",
            "discount_price",
        )


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"
