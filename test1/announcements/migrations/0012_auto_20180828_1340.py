# Generated by Django 2.1 on 2018-08-28 05:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0011_auto_20180828_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2018, 8, 28, 13, 40, 39, 369909)),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Last Modified'),
        ),
    ]