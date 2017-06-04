#!/home/tingle/anaconda2/bin/python

import matplotlib.dates as mdates
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine 



engine = create_engine('postgresql://postgres@localhost:5432/postgres')

instrument = 'EUR_USD'
fromDate = '2017-05-22 00:00:00'
toDate = '2017-05-23 00:00:00'
period = '5min'
fromtbl = 'oanda_%s_m1' % (instrument)


win_agg_group_sql = '''
  with intervals as (
  select start, start + interval '%s' as end
  from generate_series('%s', '%s', interval '%s') as start
  )
  select distinct
  intervals.start as dt,
  min(ask_l) over w as low,
  max(ask_h) over w as high,
  first_value(ask_o) over w as open,
  last_value(ask_c) over w as close,
  sum(v) over w as volume
  from
  intervals
  join %s tmb on
  tmb.dt >= intervals.start and
  tmb.dt < intervals.end
  window w as (partition by intervals.start)
  order by intervals.start;
''' % (period,fromDate,toDate,period,fromtbl)


df = pd.read_sql_query(win_agg_group_sql, 
                       con=engine)

df.dt = pd.to_datetime(df.dt)

df['21m']=np.round(pd.Series(df['close']).rolling(window=21).mean(),decimals=5)
df['55m']=np.round(pd.Series(df['close']).rolling(window=55).mean(),decimals=5)
df['21ew']=df['close'].ewm(span=21, min_periods=21).mean()
df['55ew']=df['close'].ewm(span=55, min_periods=55).mean()

#print df['21ew']

df[['close','21ew','55ew']].plot(grid=True,figsize=(8,5))
plt.show()




