# Generated by Django 2.1 on 2018-08-28 01:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0004_auto_20180828_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 28, 1, 39, 19, 58628, tzinfo=utc), verbose_name='Date of Posting'),
        ),
    ]