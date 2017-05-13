#!/usr/bin/env python

from __future__ import unicode_literals
import sys,os,getopt,re,time
import django
import datetime
from django.conf import settings
from django.db import models

sys.path.append("/home/tingle/git/eab/forexsys")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "forexsys.settings") 
django.setup()

from oanda.models import EUR_USD_M1
from django.utils import timezone

import psycopg2,psycopg2.extras
import urllib2
try:
    import simplejson as json
except ImportError:
    import json


print os.environ['okey']
print os.environ['ouser']



p = EUR_USD_M1(dt=timezone.now(),ask_o=1.11111,ask_h=1.22222,ask_l=1.33333,ask_c=1.44444,bid_o=1.11111,bid_h=1.22222,bid_l=1.33333,bid_c=1.44444,v=100)
time.sleep(1)
p = EUR_USD_M1(dt=timezone.now(),ask_o=1.11111,ask_h=1.22222,ask_l=1.33333,ask_c=1.44444,bid_o=1.11111,bid_l=1.33333,bid_c=1.44444,v=100)
p.save()




