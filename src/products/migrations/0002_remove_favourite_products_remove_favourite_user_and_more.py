# Generated by Django 5.1.2 on 2024-11-13 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="favourite",
            name="products",
        ),
        migrations.RemoveField(
            model_name="favourite",
            name="user",
        ),
        migrations.DeleteModel(
            name="Cart",
        ),
        migrations.DeleteModel(
            name="Favourite",
        ),
    ]
