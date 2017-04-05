from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
# Create your models here.


class fastTable(models.Model):
    symname = models.CharField(max_length=25)
    dt  = models.DateTimeField()
    o   = models.FloatField()
    l   = models.FloatField()
    h   = models.FloatField()
    c   = models.FloatField()
    v   = models.IntegerField()

