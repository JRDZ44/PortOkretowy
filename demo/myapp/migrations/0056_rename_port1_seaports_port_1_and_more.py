# Generated by Django 5.0.6 on 2024-06-16 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0055_rename_name1_seaports_name_remove_seaports_name2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seaports',
            old_name='port1',
            new_name='Port 1',
        ),
        migrations.RenameField(
            model_name='seaports',
            old_name='port2',
            new_name='Port 2',
        ),
        migrations.RenameField(
            model_name='seaports',
            old_name='port3',
            new_name='Port 3',
        ),
        migrations.RenameField(
            model_name='seaports',
            old_name='port4',
            new_name='Port 4',
        ),
        migrations.RenameField(
            model_name='seaports',
            old_name='port5',
            new_name='Port 5',
        ),
        migrations.RenameField(
            model_name='seaports',
            old_name='port6',
            new_name='Port 6',
        ),
    ]
