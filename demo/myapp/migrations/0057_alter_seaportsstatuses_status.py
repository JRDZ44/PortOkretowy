# Generated by Django 5.0.6 on 2024-06-16 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0056_rename_port1_seaports_port_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seaportsstatuses',
            name='status',
            field=models.IntegerField(choices=[(1, 'Aktywny'), (0, 'Nieaktywny')], default=1),
        ),
    ]
