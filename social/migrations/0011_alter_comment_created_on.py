# Generated by Django 3.2.4 on 2021-08-23 06:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0010_alter_comment_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 23, 6, 3, 5, 537254, tzinfo=utc)),
        ),
    ]