from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class TempTableModel(models.Model):
    """
    """
    dt         = models.DateTimeField()
    sym        = models.CharField(max_length=10)
    o          = models.FloatField(max_length=5,blank=True,null=True)
    h          = models.FloatField(max_length=5,blank=True,null=True)
    l          = models.FloatField(max_length=5,blank=True,null=True)
    c          = models.FloatField(max_length=5,blank=True,null=True)
    v          = models.IntegerField()

    class Meta:
        unique_together = ('sym', 'dt',)


class EUR_USD(models.Model):
    """
    """
    dt         = models.DateTimeField(null=False,unique=True)
    ask_o      = models.FloatField(max_length=10,blank=True,null=True)
    ask_h      = models.FloatField(max_length=10,blank=True,null=True)
    ask_l      = models.FloatField(max_length=10,blank=True,null=True)
    ask_c      = models.FloatField(max_length=10,blank=True,null=True)
    bid_o      = models.FloatField(max_length=10,blank=True,null=True)
    bid_h      = models.FloatField(max_length=10,blank=True,null=True)
    bid_l      = models.FloatField(max_length=10,blank=True,null=True)
    bid_c      = models.FloatField(max_length=10,blank=True,null=True)
    v          = models.IntegerField()


