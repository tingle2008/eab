#!/usr/bin/env python
# this py file can be an example for other outside script of django

from __future__ import unicode_literals
import sys,os,getopt,re
import django
import datetime
from django.conf import settings
from django.db import models

sys.path.append("/home/tingle/git/eab/forexsys")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "forexsys.settings") 
django.setup()

from oanda.models import OANDA_INSTRUMNT
import v20



def main(argv):
    for (k,v) in OANDA_INSTRUMNT:
        print '%s:%s' % (k,v)


if __name__ == "__main__":
    main(sys.argv[1:])


