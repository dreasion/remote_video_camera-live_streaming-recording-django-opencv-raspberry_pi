# Generated by Django 3.0.7 on 2020-06-29 10:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20200629_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 29, 3, 11, 57, 814209)),
        ),
    ]
