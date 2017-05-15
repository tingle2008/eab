#!/usr/bin/env python

from __future__ import unicode_literals
import sys
sys.path.append("/home/tingle/git/eab/forexsys")
sys.path.append("/home/tingle/git/eab/tools")

import os,getopt,re,time
import datetime
import pytz
import django
from django.conf import settings
from django.db import models
from django.utils.dateparse import parse_datetime
from django.db.models import Avg, Max, Min, Sum


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "forexsys.settings")
django.setup()

#from oanda.models import OANDA_INSTRUMNT,USD_JPY_M1
from oanda.models import *
from django.apps import apps

import argparse
import common.config
import common.args


class CandlePrinter(object):
    def __init__(self):
        self.width = {
            'time' : 19,
            'type' : 4,
            'price' : 8,
            'volume' : 6,
        }
        # setattr(self.width, "time", 19)
        self.time_width = 19

    def print_header(self):
        print("{:<{width[time]}} {:<{width[type]}} {:<{width[price]}} {:<{width[price]}} {:<{width[price]}} {:<{width[price]}} {:<{width[volume]}}".format(
            "Time",
            "Type",
            "Open",
            "High",
            "Low",
            "Close",
            "Volume",
            width=self.width
        ))

        print("{} {} {} {} {} {} {}".format(
            "=" * self.width['time'],
            "=" * self.width['type'],
            "=" * self.width['price'],
            "=" * self.width['price'],
            "=" * self.width['price'],
            "=" * self.width['price'],
            "=" * self.width['volume']
        ))


    def indb_candle(self, candle,inst_str):
        try:
            time = str(
                datetime.strptime(
                    candle.time,
                    "%Y-%m-%dT%H:%M:%S.000000000Z"
                )
            )
        except:
            time = candle.time.split(".")[0]

        volume = candle.volume

        inst_model_name = '%s_M1' % inst_str
        inst_model = apps.get_model( 'oanda' , inst_model_name )

        b = getattr(candle,'bid',None)
        a = getattr(candle,'ask',None)

        naive_time = parse_datetime(time)

        p = inst_model(dt=pytz.timezone("Zulu").localize(naive_time, is_dst=None),
                       ask_o=a.o,
                       ask_h=a.h,
                       ask_l=a.l,
                       ask_c=a.c,
                       bid_o=b.o,
                       bid_h=b.h,
                       bid_l=b.l,
                       bid_c=b.c,
                       v=volume)

        p.save()

        volume = ""
        time = ""
        p = ""


def get_latest_dt( inst_str ):

    inst_model_name = '%s_M1' % inst_str
    inst_model = apps.get_model( 'oanda' , inst_model_name )
    maxdt = '2005-01-01T01:00:00.000000000Z'

    if inst_model.objects.all().aggregate(Max('dt'))['dt__max']:
        mdt = inst_model.objects.all().aggregate(Max('dt'))['dt__max'] + datetime.timedelta(minutes=1) 
        maxdt = mdt.strftime('%Y-%m-%dT%H:%M:%S.000000000Z')

    return maxdt

def main(argv):

    kwargs = {"granularity":'M1' , "price":'AB' , "smooth":False , "fromTime":'2005-01-01T01:00:00.000000000Z' }
    parser = argparse.ArgumentParser()
    common.config.add_argument(parser)

    parser.add_argument(
        "instrument",
        type=common.args.instrument,
        help="The instrument to get candles for"
    )

    args = parser.parse_args()
    instrument = args.instrument
    api = args.config.create_context()

    while True:
        mdt = get_latest_dt( instrument )
        f_sec = time.mktime(datetime.datetime.strptime(kwargs["fromTime"],"%Y-%m-%dT%H:%M:%S.000000000Z").timetuple())
        m_sec = time.mktime(datetime.datetime.strptime(mdt,"%Y-%m-%dT%H:%M:%S.000000000Z").timetuple())

        print 'f_sec,m_sec is [%s]:[%s]' % (f_sec,m_sec)
        if (m_sec - f_sec) <= 60:
            print 'MaxTime:fromTime diff less than 1 minus'
            break

        kwargs["fromTime"] = mdt
        #
        # Fetch the candles
        #
        response = api.instrument.candles(instrument, **kwargs)

        if response.status != 200:
            print(response)
            print(response.body)
            return

        printer = CandlePrinter()
        #printer.print_header()
        candles = response.get("candles", 200)

        for candle in response.get("candles", 200):
            printer.indb_candle(candle,instrument)

if __name__ == "__main__":
    main(sys.argv[1:])


