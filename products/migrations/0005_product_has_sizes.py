# Generated by Django 3.2.9 on 2021-11-11 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_product_quantity_available"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="has_sizes",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
