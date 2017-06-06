#!/usr/bin/env Rscript



require("RPostgreSQL")
require("xts")
library(quantmod)

pw <- {
  "1Ve46scoS"
}
# host <- 'localhost'

host <- '125.208.20.140'

drv <- dbDriver("PostgreSQL")

con <- dbConnect(drv, dbname = "hifive",
                 host = host, port = 5432,
                 user = "hifive", password=pw)


instrument <- 'EUR_USD'
fromDate <- '2010-07-10 00:00:00'
toDate <- '2010-07-15 23:59:00'
period <- '5min'
fromtbl <- paste("oanda",instrument,"m1", sep = '_')

win_agg_group_sql <- paste("  with intervals as (
  select start, start + interval '", period ,"' as end
  from generate_series('" , fromDate , "', '", toDate,"', interval '", period ,"' ) as start
  )
  select distinct
  intervals.start as dt,
  min(bid_l) over w as low,
  max(bid_h) over w as high,
  first_value(bid_o) over w as open,
  last_value(bid_c) over w as close,
  sum(v) over w as volume
  from
  intervals
  join ",fromtbl," tmb on
  tmb.dt >= intervals.start and
  tmb.dt < intervals.end
  window w as (partition by intervals.start)
  order by intervals.start; "
)


inst_df <- dbGetQuery(con,win_agg_group_sql)

inst_xts <- xts(as.matrix(inst_df[,-1]), order.by=inst_df[,1])

candleChart(inst_xts)