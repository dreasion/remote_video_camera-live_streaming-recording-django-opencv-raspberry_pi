# Generated by Django 3.0.7 on 2020-07-02 00:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_auto_20200701_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 17, 50, 40, 960353)),
        ),
    ]
