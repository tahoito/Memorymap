# Generated by Django 5.1.6 on 2025-02-20 02:49

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_alter_diary_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('memo', models.TextField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='diary',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 20, 2, 49, 22, 743810, tzinfo=datetime.timezone.utc), verbose_name='作成日時'),
        ),
    ]
