from django.conf import settings
from django.utils import timezone
from django.dispatch import receiver
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.translation import (
    gettext_lazy as _,
)
from django_softdelete.models import SoftDeleteModel
from datetime_validators.validators import date_time_is_future_validator


class Product(SoftDeleteModel):
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
    created = models.DateTimeField(
        _("Created At"),
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        _("Modified At"),
        auto_now=True,
    )

    @property
    def thumbnail(self):
        return self.attachments.first()

    @property
    def discount_price(self):
        if self.discount and self.discount.is_active():
            return self.discount.price

    def __str__(self):
        return self.title


class Discount(models.Model):
    product = models.OneToOneField(
        "products.Product",
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(
        _("Price"),
        max_digits=10,
        decimal_places=2,
        help_text=_("Price of the product"),
    )
    starting_from = models.DateTimeField(
        _("Starting From"),
        null=True,
    )
    ending_at = models.DateTimeField(
        _("Ending At"),
        null=True,
        validators=[date_time_is_future_validator],
    )

    def __str__(self):
        return str(self.price)

    def is_active(self):
        if not self.starting_from:
            return False
        if self.starting_from < timezone.now() and not self.ending_at:
            return True
        if self.starting_from < timezone.now() < self.ending_at:
            return True
        return False


@receiver(models.signals.post_save, sender=Product)
def create_discount(sender, instance, created, **kwargs):
    if created:
        Discount.objects.create(product=instance, price=instance.price)
