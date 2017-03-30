# -*- coding: utf-8 -*-
# Author: Yang GAO<kingjiyangATgmail.com>

from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class Lend(models.Model):
    """
    """
    user                = models.OneToOneField(User, unique=True)
    debit_name          = models.CharField(max_length=50)
    debit_phone         = models.CharField(max_length = 50)
    interest_rate     = models.FloatField(max_length=5,blank=True,null=True)
    interest_sum      = models.FloatField(max_length=5,blank=True,null=True)
    lend_date         = models.DateField()
    repay_date        = models.DateField()
    order_id          = models.CharField(max_length=12)




class Borrow(models.Model):
    """
    """
    user                = models.OneToOneField(User, unique=True)
    repay_date          = models.DateField()
    

        
        
  
