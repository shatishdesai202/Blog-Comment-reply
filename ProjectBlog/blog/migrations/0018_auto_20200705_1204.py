# Generated by Django 3.0.5 on 2020-07-05 06:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20200705_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 5, 12, 4, 38, 145315)),
        ),
    ]
