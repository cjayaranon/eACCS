# Generated by Django 2.1 on 2018-08-22 00:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0013_auto_20180816_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_post',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 22, 8, 30, 26, 639092), verbose_name='Date of Posting'),
        ),
    ]