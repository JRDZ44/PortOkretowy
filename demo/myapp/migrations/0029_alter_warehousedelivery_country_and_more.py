# Generated by Django 5.0.6 on 2024-06-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_alter_warehousedelivery_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehousedelivery',
            name='country',
            field=models.SlugField(choices=[('PL', 'Polska'), ('DE', 'Niemcy'), ('FR', 'Francja'), ('ES', 'Hiszpania'), ('IT', 'Włochy')], default=[('PL', 'Polska'), ('DE', 'Niemcy'), ('FR', 'Francja'), ('ES', 'Hiszpania'), ('IT', 'Włochy')], max_length=200),
        ),
        migrations.AlterField(
            model_name='warehousedelivery',
            name='country1',
            field=models.SlugField(choices=[('PL', 'Polska'), ('DE', 'Niemcy'), ('FR', 'Francja'), ('ES', 'Hiszpania'), ('IT', 'Włochy')], default=[('PL', 'Polska'), ('DE', 'Niemcy'), ('FR', 'Francja'), ('ES', 'Hiszpania'), ('IT', 'Włochy')], max_length=200),
        ),
        migrations.AlterField(
            model_name='warehousedelivery',
            name='country2',
            field=models.SlugField(choices=[('PL', 'Polska'), ('DE', 'Niemcy'), ('FR', 'Francja'), ('ES', 'Hiszpania'), ('IT', 'Włochy')], default=[('PL', 'Polska'), ('DE', 'Niemcy'), ('FR', 'Francja'), ('ES', 'Hiszpania'), ('IT', 'Włochy')], max_length=200),
        ),
    ]