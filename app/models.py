from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    #todo_job = models.TextField()
    #created_date = models.DateTimeField(editable=False , default=datetime.now())
    #name = models.ForeignKey('auth.User',null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title