# Generated by Django 3.2.4 on 2021-08-22 13:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_auto_20210822_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 22, 13, 55, 25, 500695, tzinfo=utc)),
        ),
    ]