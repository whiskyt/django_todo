# Generated by Django 3.2 on 2021-04-30 00:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0012_alter_todo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 0, 35, 13, 267063, tzinfo=utc)),
        ),
    ]
