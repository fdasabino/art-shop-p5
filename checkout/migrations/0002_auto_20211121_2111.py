# Generated by Django 3.2.9 on 2021-11-21 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-date',)},
        ),
        migrations.RemoveField(
            model_name='order',
            name='county',
        ),
    ]
