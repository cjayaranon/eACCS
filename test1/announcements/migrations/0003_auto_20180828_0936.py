# Generated by Django 2.1 on 2018-08-28 01:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0002_auto_20180828_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='date_post',
        ),
        migrations.AddField(
            model_name='announcement',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 28, 9, 36, 58, 577080), verbose_name='Date of Posting'),
        ),
    ]
