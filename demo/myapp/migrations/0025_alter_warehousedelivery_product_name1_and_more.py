# Generated by Django 5.0.6 on 2024-06-02 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_alter_warehousedelivery_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehousedelivery',
            name='product_name1',
            field=models.CharField(default='WarehouseDelivery1', max_length=100),
        ),
        migrations.AlterField(
            model_name='warehousedelivery',
            name='product_name2',
            field=models.CharField(default='WarehouseDelivery2', max_length=100),
        ),
    ]
