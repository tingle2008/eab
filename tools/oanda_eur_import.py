#!/usr/bin/env python

from __future__ import unicode_literals
import sys,os,getopt,re,time
import pytz
import django
from django.conf import settings
from django.db import models
from django.utils.dateparse import parse_datetime
from django.db.models import Avg, Max, Min, Sum

sys.path.append("/home/tingle/git/eab/forexsys")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "forexsys.settings")
django.setup()

from oanda.models import OANDA_INSTRUMNT,EUR_USD_M1

import argparse
import common.config
import common.args
import datetime

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

    def print_candle(self, candle):
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

        for price in ["mid", "bid", "ask"]:
            c = getattr(candle, price, None)

            if c is None:
                continue

            print("{:>{width[time]}} {:>{width[type]}} {:>{width[price]}} {:>{width[price]}} {:>{width[price]}} {:>{width[price]}} {:>{width[volume]}}".format(
                time,
                price,
                c.o,
                c.h,
                c.l,
                c.c,
                volume,
                width=self.width
            ))

            volume = ""
            time = ""


    def indb_candle(self, candle):
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

        b = getattr(candle,'bid',None)
        a = getattr(candle,'ask',None)


        naive_time = parse_datetime(time)

        p = EUR_USD_M1(dt=pytz.timezone("Zulu").localize(naive_time, is_dst=None),
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


def get_latest_dt():

    if EUR_USD_M1.objects.all().aggregate(Max('dt'))['dt__max']:
        mdt = EUR_USD_M1.objects.all().aggregate(Max('dt'))['dt__max'] + datetime.timedelta(minutes=1) 
        maxdt = mdt.strftime('%Y-%m-%dT%H:%M:%S.000000000Z')
        
    else:
        maxdt = '2005-01-01T01:00:00.000000000Z'
        
    return maxdt


def main():

    kwargs = {}
    kwargs["granularity"] = 'M1'
    kwargs["price"] = 'AB'
    kwargs["smooth"] = False
    instrument = 'EUR_USD'
    kwargs["fromTime"] = ''
    parser = argparse.ArgumentParser()
    common.config.add_argument(parser)
    args = parser.parse_args()
    api = args.config.create_context()


    while True:
        mdt = get_latest_dt()
        if kwargs["fromTime"] == mdt:
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

        printer.print_header()

        candles = response.get("candles", 200)

        for candle in response.get("candles", 200):
            printer.indb_candle(candle)

    #api.datetime_to_str(args.from_time)
    #print me(EUR_USD_M1.objects.all().aggregate(Max('dt')))

if __name__ == "__main__":
    main()


