# Generated by Django 3.1.6 on 2021-02-18 15:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201210_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 18, 22, 34, 28, 726321), verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='article',
            name='modify_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 18, 22, 34, 28, 726321), verbose_name='Last Modified'),
        ),
    ]
