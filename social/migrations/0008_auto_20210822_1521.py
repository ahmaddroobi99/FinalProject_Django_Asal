# Generated by Django 3.2.4 on 2021-08-22 12:21

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0007_auto_20210822_1517'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserPofile',
            new_name='UserProfile',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 22, 12, 21, 28, 533898, tzinfo=utc)),
        ),
    ]
