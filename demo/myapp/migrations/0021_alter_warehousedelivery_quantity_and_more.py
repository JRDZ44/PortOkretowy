# Generated by Django 5.0.6 on 2024-06-02 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_warehousedelivery_quantity1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehousedelivery',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='warehousedelivery',
            name='quantity1',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='warehousedelivery',
            name='quantity2',
            field=models.PositiveIntegerField(),
        ),
    ]