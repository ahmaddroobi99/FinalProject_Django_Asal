# Generated by Django 3.2.4 on 2021-08-23 08:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0012_auto_20210823_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 23, 8, 7, 26, 85007, tzinfo=utc)),
        ),
    ]