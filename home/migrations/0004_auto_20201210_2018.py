# Generated by Django 3.1.4 on 2020-12-10 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201209_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 10, 20, 18, 51, 620540), verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='article',
            name='modify_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 10, 20, 18, 51, 620540), verbose_name='Last Modified'),
        ),
    ]
