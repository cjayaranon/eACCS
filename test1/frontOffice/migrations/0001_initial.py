# Generated by Django 2.1 on 2018-08-16 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('firstName', models.CharField(max_length=20)),
                ('middleName', models.CharField(max_length=20)),
                ('suffix', models.CharField(blank=True, max_length=3)),
                ('birthdate', models.DateField()),
                ('sex', models.CharField(max_length=6)),
                ('civilStatus', models.CharField(max_length=20)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=4)),
                ('height', models.CharField(max_length=4)),
                ('monthlyIncome', models.DecimalField(decimal_places=2, max_digits=8)),
                ('profession', models.CharField(max_length=30)),
                ('mailingAddress1', models.TextField()),
                ('mailingAddress2', models.TextField(default='')),
                ('sameMailingAddress', models.BooleanField(default=False)),
                ('clientPhoto', models.ImageField(upload_to='clients/images/%Y-%m-%d/')),
                ('clientSignature', models.ImageField(upload_to='clients/signatures/%Y-%m-%d/')),
            ],
        ),
    ]
