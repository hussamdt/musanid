# Generated by Django 4.0.1 on 2022-01-08 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20210220_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Time'),
        ),
    ]
