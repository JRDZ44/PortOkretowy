# Generated by Django 5.0.6 on 2024-06-02 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_remove_warehousedelivery_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehousedelivery',
            name='product_name',
            field=models.CharField(default='Warehouse Delivery', max_length=100),
        ),
    ]
