# Generated by Django 5.0.6 on 2024-06-15 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0048_container_sum1_container_sum2_container_sum3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='container_code1',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='container',
            name='container_code2',
            field=models.CharField(default=10, max_length=100),
        ),
        migrations.AddField(
            model_name='container',
            name='container_code3',
            field=models.CharField(default=20, max_length=100),
        ),
        migrations.AddField(
            model_name='container',
            name='container_code4',
            field=models.CharField(default=30, max_length=100),
        ),
        migrations.AddField(
            model_name='container',
            name='container_code5',
            field=models.CharField(default=40, max_length=100),
        ),
    ]