# Generated by Django 3.2.9 on 2021-11-22 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_quantity_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_sizes',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.AddField(
            model_name='product',
            name='sold_out',
            field=models.BooleanField(default='False'),
        ),
    ]
