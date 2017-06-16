#!/usr/bin/env python

from metatrader.mt4 import initizalize
from metatrader.backtest import BackTest
from datetime import datetime


# point mt4 install folder
initizalize('/export/crawlspace/mt4-land/oanda-01')


from_date = datetime(2017, 6, 1)
to_date = datetime(2017, 6, 15)

ea_name = 'ema_cross_ea'


param = {
         'Lots': {'value': 0.01}
         }

backtest = BackTest(ea_name, param, 'EURUSD-2', 'M5', from_date, to_date,model=0)



ret = backtest.run()
print ret.gross_profit
