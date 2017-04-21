# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from datetime import datetime, timedelta

from django.db import models


class Todo(models.Model):

    todo = models.CharField(max_length=64)
    flag = models.IntegerField(default=0)                  # 0 represent undo, 1 represent complete
    priority = models.IntegerField(default=0)              # 0 represent common, 1 represent prior
    create_time = models.DateTimeField(auto_now_add=True)
    expire_time = models.DateTimeField(default=datetime.now()+timedelta(days=1))

    def __unicode__(self):
        return u"%d %s %d" % (self.id, self.todo, self.flag)

    class Meta:
        ordering = ["priority", "expire_time"]
