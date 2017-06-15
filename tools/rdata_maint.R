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
  e$xts_name = sprintf("oanda.%s.1minutes",tolower(inst))

  stopifnot(is.xts( get(e$xts_name) ))
  
  return(format(max(index(get(e$xts_name))),format='%Y-%m-%d %H:%M:%S %Z'))
}

pg_max_dt <- function(inst) {
  e<<-new.env()
  e$max_date_sql <- sprintf("select max(dt) from oanda_%s_m1",inst)
  e$max_date <- dbGetQuery(conn(),e$max_date_sql)
  return(format(e$max_date[1,1],format='%Y-%m-%d %H:%M:%S %Z'))
}


load_inst_from <- function(inst,fromDt='2005-01-01 23:59:59 GMT',toDt,p='1min') {

  if( ! p %in% c('1min','5min','15min','30min') ) {
    return(FALSE)
  }

  local_inst_obj = sprintf("oanda.%s.%s",tolower(inst),p)

  if( p == '1min') {
    sql_str = sprintf("select dt,bid_o as open,
                               bid_h as high,
                               bid_l as low,
                               bid_c as close from oanda_%s_m1
                               where dt > '%s'::timestamp with time zone order by dt",tolower(inst),fromDt)
  } else {
    sql_str = sprintf("with intervals as (
                      select start, start + interval '%s' as end
                      from generate_series('%s', '%s', interval '%s' ) as start
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
                      join oanda_%s_m1 tmb on
                      tmb.dt >= intervals.start and
                      tmb.dt < intervals.end
                      window w as (partition by intervals.start)
                      order by intervals.start; " , p,fromDt,toDt,p,inst)
  }

  cat("sql_str is:",sql_str)
  inst_df <- dbGetQuery(conn(),sql_str)
  head(inst_df)
  assign(local_inst_obj,xts(as.matrix(inst_df[,-1]), order.by=inst_df[,1]),envir = .GlobalEnv)
}

load_inst_from("EUR_USD",from="2017-05-31 00:00:00 GMT",'15min')



save.image()

check_and_load <- function(inst) {
  ##inst_name = sprintf("oanda.%s.m1",tolower(inst))
  inst_name = sprintf("oanda.%s.m1",tolower(inst))
  if(! exists(inst_name) ) {
    cat(inst_name," doesnt exists\n")
    return(FALSE)
  }

  return(TRUE)
}

check_and_load("EUR_USD")

xts_max_dt("EUR_USD")
pg_max_dt("EUR_USD")

as.POSIXct(xts_max_dt("EUR_USD")) - as.POSIXct(pg_max_dt("EUR_USD"))


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


