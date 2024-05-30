from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.translation import (
    gettext_lazy as _,
)
from django_softdelete.models import SoftDeleteModel
from datetime_validators.validators import date_time_is_future_validator


class Product(SoftDeleteModel):
    title = models.CharField(
        _("Title"), max_length=100, help_text=_("Title of the product")
    )
    description = models.TextField(
        _("Description"), blank=True, help_text=_("Description of the product")
    )
    price = models.DecimalField(
        _("Price"),
        max_digits=10,
        decimal_places=2,
        help_text=_("Price of the product"),
    )
    quantity = models.PositiveIntegerField(
        _("Quantity"), help_text=_("Quantity of the product")
    )
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    attachments = GenericRelation(
        "attachments.Attachment",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        _("Created At"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _("Updated At"),
        auto_now=True,
    )

    @property
    def thumbnail(self):
        return self.attachments.first()

    def __str__(self):
        return self.title


class Discount(models.Model):
    price = models.DecimalField(
        _("Price"),
        max_digits=10,
        decimal_places=2,
        help_text=_("Price of the product"),
    )

    starting_from = models.DateTimeField(
        _("Starting From"),
    )
    ending_at = models.DateTimeField(
        _("Ending At"),
        validators=[date_time_is_future_validator],
    )
