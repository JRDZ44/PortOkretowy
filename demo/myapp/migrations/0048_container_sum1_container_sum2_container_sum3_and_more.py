# Generated by Django 5.0.6 on 2024-06-09 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0047_alter_warehousedelivery_country1'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='sum1',
            field=models.CharField(default=10, max_length=100),
        ),
        migrations.AddField(
            model_name='container',
            name='sum2',
            field=models.CharField(default=10, max_length=100),
        ),
        migrations.AddField(
            model_name='container',
            name='sum3',
            field=models.CharField(default=10, max_length=100),
        ),
        migrations.AddField(
            model_name='container',
            name='sum4',
            field=models.CharField(default=10, max_length=100),
        ),
        migrations.AddField(
            model_name='container',
            name='sum5',
            field=models.CharField(default=10, max_length=100),
        ),
        migrations.AlterField(
            model_name='container',
            name='sum',
            field=models.CharField(default=10, max_length=100),
        ),
    ]
