# Generated by Django 3.0.7 on 2020-06-28 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_records_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='time',
            field=models.TimeField(auto_now=True, null=True),
        ),
    ]
