# Generated by Django 3.0.7 on 2020-06-28 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200627_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='records',
            name='time',
        ),
    ]
