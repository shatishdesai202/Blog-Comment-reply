# Generated by Django 3.0.5 on 2020-07-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200704_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
