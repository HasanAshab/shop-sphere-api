from django.contrib import admin
from attachments.admin import AttachmentInlines
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (AttachmentInlines,)
