# Generated by Django 5.0.6 on 2024-06-16 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0053_warehousedelivery_seaports'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seaports',
            name='name',
        ),
        migrations.AddField(
            model_name='seaports',
            name='name1',
            field=models.CharField(default='port', max_length=130),
        ),
        migrations.AddField(
            model_name='seaports',
            name='name2',
            field=models.CharField(default='port', max_length=130),
        ),
        migrations.AddField(
            model_name='seaports',
            name='name3',
            field=models.CharField(default='port', max_length=130),
        ),
        migrations.AddField(
            model_name='seaports',
            name='name4',
            field=models.CharField(default='port', max_length=130),
        ),
        migrations.AddField(
            model_name='seaports',
            name='name5',
            field=models.CharField(default='port', max_length=130),
        ),
        migrations.AddField(
            model_name='seaports',
            name='name6',
            field=models.CharField(default='port', max_length=130),
        ),
    ]
