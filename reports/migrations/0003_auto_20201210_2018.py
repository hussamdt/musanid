# Generated by Django 3.1.4 on 2020-12-10 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20201209_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='time',
            field=models.DateTimeField(verbose_name='Time'),
        ),
    ]
