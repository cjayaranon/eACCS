# Generated by Django 2.1 on 2018-08-30 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0023_auto_20180828_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='date_posted',
            new_name='date_pub',
        ),
    ]