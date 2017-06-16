#!/usr/bin/python

from metatrader.mt4 import initizalize
from metatrader.backtest import BackTest

# point mt4 install folder
initizalize('C:\\Program Files\\FXCM MetaTrader 4')

# # specify backtest period by datetime format
# from_date = datetime(2017, 6, 1)
# to_date = datetime(2017, 6, 15)

# ea_name = 'Moving Average'

# # create ea param by dict.
# param = {
#          'Lots': {'value': 0.1},
#          'MaximumRisk': {'value': 0.02},
#          'DecreaseFactor': {'value': 3.0},
#          'MovingPeriod': {'value': 12},
#          'MovingShift': {'value': 6}
#          }
# # create backtest object
# backtest = BackTest(ea_name, param, 'USDJPY', 'M5', from_date, to_date)

# # create backtest object with specified spread
# # backtest = BackTest(ea_name, param, 'USDJPY', 'M5', from_date, to_date, spread=10)

# # run backtest
# ret = backtest.run()

# # you can get result from result object
# # for example you can print gross profit
# print ret.gross_profit
