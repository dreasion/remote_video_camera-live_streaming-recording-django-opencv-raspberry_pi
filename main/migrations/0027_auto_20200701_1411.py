# Generated by Django 3.0.7 on 2020-07-01 21:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20200630_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 14, 11, 5, 105973)),
        ),
    ]
