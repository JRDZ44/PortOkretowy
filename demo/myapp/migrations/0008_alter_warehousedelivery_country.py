# Generated by Django 5.0.6 on 2024-06-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_warehousedelivery_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehousedelivery',
            name='country',
            field=models.SlugField(choices=[('PL', 'Polska'), ('DE', 'Niemcy'), ('FR', 'Francja'), ('ES', 'Hiszpania'), ('IT', 'Włochy')], default='PL', max_length=90),
        ),
    ]
