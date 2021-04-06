# Generated by Django 3.0.6 on 2020-06-03 21:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='data_publicacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 3, 18, 38, 53, 198947)),
        ),
    ]
