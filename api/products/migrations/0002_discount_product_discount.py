# Generated by Django 5.0 on 2024-06-01 04:46

import datetime_validators.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Discount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Price of the product",
                        max_digits=10,
                        verbose_name="Price",
                    ),
                ),
                (
                    "starting_from",
                    models.DateTimeField(verbose_name="Starting From"),
                ),
                (
                    "ending_at",
                    models.DateTimeField(
                        validators=[
                            datetime_validators.validators.date_time_is_future_validator
                        ],
                        verbose_name="Ending At",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="discount",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="products.discount",
            ),
        ),
    ]
