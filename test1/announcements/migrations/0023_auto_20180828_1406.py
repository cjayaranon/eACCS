# Generated by Django 2.1 on 2018-08-28 06:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0022_auto_20180828_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_posted',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Publication Schedule'),
        ),
    ]