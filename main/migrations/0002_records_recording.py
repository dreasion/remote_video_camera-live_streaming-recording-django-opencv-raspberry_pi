# Generated by Django 3.0.7 on 2020-06-28 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='recording',
            field=models.BooleanField(default=False),
        ),
    ]
