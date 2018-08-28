# Generated by Django 2.1 on 2018-08-28 05:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0010_auto_20180828_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='last_modified',
            field=models.DateField(auto_now=True, verbose_name='Last Modified'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2018, 8, 28, 13, 39, 15, 465842)),
        ),
    ]