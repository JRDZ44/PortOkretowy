# Generated by Django 5.0.6 on 2024-06-08 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_alter_warehousedelivery_country3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehousedelivery',
            name='country6',
        ),
        migrations.RemoveField(
            model_name='warehousedelivery',
            name='product_name6',
        ),
    ]
