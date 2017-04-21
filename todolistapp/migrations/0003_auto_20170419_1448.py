# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todolistapp', '0002_remove_todo_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['priority', 'expire_time']},
        ),
        migrations.RemoveField(
            model_name='todo',
            name='deadline',
        ),
        migrations.AddField(
            model_name='todo',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 20, 14, 48, 14, 491000)),
        ),
    ]
