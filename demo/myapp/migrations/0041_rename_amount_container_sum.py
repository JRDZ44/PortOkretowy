# Generated by Django 5.0.6 on 2024-06-09 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0040_alter_container_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='container',
            old_name='amount',
            new_name='sum',
        ),
    ]
