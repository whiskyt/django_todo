# Generated by Django 3.2 on 2021-04-30 00:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0018_alter_todo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 0, 51, 33, 582070, tzinfo=utc)),
        ),
    ]
