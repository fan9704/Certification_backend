# Generated by Django 4.0 on 2022-01-15 11:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('restfulapi', '0011_rename_user_message_username_alter_message_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 15, 11, 25, 55, 190282, tzinfo=utc)),
        ),
    ]