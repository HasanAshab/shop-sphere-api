# Generated by Django 5.0 on 2024-05-12 03:32

import django.contrib.auth.validators
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermodel",
            name="avatar",
            field=models.ImageField(
                blank=True,
                default="",
                help_text="Avatar (profile picture) of the user",
                upload_to="uploads/avatars/",
                verbose_name="Avatar",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="usermodel",
            name="name",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Name of the user",
                max_length=255,
                verbose_name="Name",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="usermodel",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                default="",
                help_text="Phone number of the user",
                max_length=128,
                region=None,
                verbose_name="Phone Number",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="usermodel",
            name="username",
            field=models.CharField(
                error_messages={
                    "unique": "A user with that username already exists."
                },
                help_text="Required. 35 characters or fewer.Letters, digits and @/./+/-/_ only.",
                max_length=35,
                unique=True,
                validators=[
                    django.contrib.auth.validators.UnicodeUsernameValidator()
                ],
                verbose_name="username",
            ),
        ),
    ]
