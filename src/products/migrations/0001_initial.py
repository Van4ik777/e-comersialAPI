# Generated by Django 5.1.2 on 2024-11-10 15:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "discount",
                    models.DecimalField(decimal_places=2, default=0, max_digits=5),
                ),
                ("description", models.TextField()),
                (
                    "images",
                    models.ImageField(blank=True, null=True, upload_to="products/"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="products.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Favourite",
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
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="favourite",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("products", models.ManyToManyField(blank=True, to="products.product")),
            ],
        ),
        migrations.CreateModel(
            name="Cart",
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
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cart",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("products", models.ManyToManyField(blank=True, to="products.product")),
            ],
        ),
        migrations.CreateModel(
            name="ProductDetail",
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
                ("colors", models.JSONField(default=list)),
                ("materials", models.JSONField(default=list)),
                (
                    "height",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "width",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "depth",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("swivel_mechanism", models.BooleanField(default=False)),
                (
                    "product",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="details",
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
