# Generated by Django 5.0.6 on 2024-06-02 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_warehousedelivery_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehousedelivery',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
