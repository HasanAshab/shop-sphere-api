from django.conf import settings
from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
from django.utils.translation import (
    gettext_lazy as _,
)


class Review(models.Model):
    rate = models.PositiveSmallIntegerField(
        _("Rate"),
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
        help_text=_("Rate of the product"),
    )
    text = models.TextField(
        _("Text"),
        blank=True,
        help_text=_("Text of the review"),
    )
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
    )
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        _("Created At"),
        auto_now_add=True,
    )

    def __str__(self):
        return self.name
