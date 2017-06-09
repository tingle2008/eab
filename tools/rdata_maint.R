#!/usr/bin/env Rscript


require("RPostgreSQL")
require("xts")
library("optparse")

option_list = list(
  make_option(c("-d", "--basedir"), type="character", default="~/rdata",
              help="local base directory", metavar="character")
);



opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);


if (is.null(opt$basedir)){
  print_help(opt_parser)
  stop("At least one argument must be supplied .n", call.=FALSE)
}


e<<-new.env()
e$rdata <- sprintf("%s/.RData",opt$basedir)
setwd(opt$basedir)
load(e$rdata)

conn <- function() {
  e<<-new.env()
  e$pw <- {
  "1Ve46scoS"
  }
  e$host <- '125.208.20.140'
  e$drv <- dbDriver("PostgreSQL")
  e$con <- dbConnect(e$drv, dbname = "hifive",
                     host = e$host, port = 5432,
                     user = "hifive", password=e$pw)

  return(e$con)
}


xts_max_dt <- function(inst) {

  e<<-new.env()
  e$xts_name = sprintf("oanda.%s.m1",tolower(inst))

  stopifnot(is.xts( get(e$xts_name) ))
  
  return(format(max(index(get(e$xts_name))),format='%Y-%m-%d %H:%M:%S %Z'))
}

pg_max_dt <- function(inst) {
  e<<-new.env()
  e$max_date_sql <- sprintf("select max(dt) from oanda_%s_m1",inst)
  e$max_date <- dbGetQuery(conn(),e$max_date_sql)
  return(format(e$max_date[1,1],format='%Y-%m-%d %H:%M:%S %Z'))
}

xts_max_dt("EUR_USD")
pg_max_dt("EUR_USD")

as.POSIXct(xts_max_dt(inst_xts)) - as.POSIXct(pg_max_dt("EUR_USD"))

stop("stop here")

db_table_fatch <- function( inst, start ,period) {
  e<<-new.env()
  e$instrument <- 'EUR_USD'
  e$fromDate   <- '2010-07-10 00:00:00'
  e$toDate     <- '2010-07-15 23:59:00'
  e$period     <- '5min'
  e$fromtbl    <- paste("oanda",instrument,"m1", sep = '_')
  return()
}


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


inst_df <- dbGetQuery(conn(),win_agg_group_sql)

inst_xts <- xts(as.matrix(inst_df[,-1]), order.by=inst_df[,1])

ls()
save.image()


