# Generated by Django 5.0.6 on 2024-06-09 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0038_alter_container_container_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
