from django.conf import settings
from django.db import models
from django.utils.translation import (
    gettext_lazy as _,
)


class Product(models.Model):
    name = models.CharField(
        _("Name"), max_length=255, help_text=_("The name of the product")
    )
    description = models.TextField(
        _("Description"), help_text=_("A description of the product")
    )
    price = models.DecimalField(
        _("Price"),
        max_digits=10,
        decimal_places=2,
        help_text=_("The price of the product"),
    )
    image = models.ImageField(
        _("Image"),
        upload_to="products/",
        null=True,
        blank=True,
        help_text=_("An image of the product"),
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        "api.categories.Category",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        _("Created At"),
        auto_now_add=True,
        help_text=_("The date and time when the product was created"),
    )
    updated_at = models.DateTimeField(
        _("Updated At"),
        auto_now=True,
        help_text=_("The date and time when the product was last updated"),
    )

    def __str__(self):
        return self.name
