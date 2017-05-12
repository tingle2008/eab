#!/usr/bin/env python


from __future__ import unicode_literals
import sys,os,django
import datetime
from django.conf import settings
from django.db import models

sys.path.append("/home/tingle/git/eab/forexsys")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "forexsys.settings") 
django.setup()

from market.models import TempTableModel
from market.models import EUR_USD

from django.utils import timezone



p = EUR_USD(dt=timezone.now(),ask_o=1.11111,ask_h=1.22222,ask_l=1.33333,ask_c=1.44444,bid_o=1.11111,bid_h=1.22222,bid_l=1.33333,bid_c=1.44444,v=100)
p = EUR_USD(dt=timezone.now(),ask_o=1.11111,ask_h=1.22222,ask_l=1.33333,ask_c=1.44444,bid_o=1.11111,bid_l=1.33333,bid_c=1.44444,v=100)
p.save()




