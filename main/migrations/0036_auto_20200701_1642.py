# Generated by Django 3.0.7 on 2020-07-01 23:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_auto_20200701_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='releative_path',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='records',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 16, 42, 27, 960133)),
        ),
    ]
