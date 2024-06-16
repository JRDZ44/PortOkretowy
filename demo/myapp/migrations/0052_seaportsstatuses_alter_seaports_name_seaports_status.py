# Generated by Django 5.0.6 on 2024-06-16 10:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0051_seaports'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeaportsStatuses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Aktywny'), (2, 'Nieaktywny')], default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='seaports',
            name='name',
            field=models.CharField(max_length=130),
        ),
        migrations.AddField(
            model_name='seaports',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.seaportsstatuses'),
        ),
    ]
