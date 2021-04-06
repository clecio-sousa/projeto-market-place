# Generated by Django 3.0.6 on 2020-06-03 23:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_auto_20200603_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='slug',
            field=models.SlugField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='data_publicacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 3, 20, 17, 42, 953278)),
        ),
    ]
