# Generated by Django 5.0.6 on 2024-06-09 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0046_alter_warehousedelivery_country1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehousedelivery',
            name='country1',
            field=models.SlugField(max_length=200),
        ),
    ]
