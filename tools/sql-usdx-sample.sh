#!/bin/sh

# ./list_usdx_component |awk -F ':' '{print $1" AS(select power(bid_o,"$2") from oanda_"$1"_m1 where dt=\x272017-05-10 00:00:00-00\x27)," }'  |sed  '1 i\with' | sed '$ s/,$//g'
# ./list_usdx_component |cut -d ':' -f 1 |sed -e '1 i\select ' -e '$ a\50.14348112 from'  -e 's/$/.power*/g'|sed -e ':a ; N;s/\n// ; t a ; '  
# ./list_usdx_component |cut -d ':' -f 1 |sed -e ':a ; N;s/\n/,/ ; t a ; '

cat << EOF
with
eur_usd AS(select power(ask_o,-0.576) from oanda_eur_usd_m1 where dt='2017-05-10 00:00:00-00'),
usd_jpy AS(select power(ask_o,0.136) from oanda_usd_jpy_m1 where dt='2017-05-10 00:00:00-00'),
gbp_usd AS(select power(ask_o,-0.119) from oanda_gbp_usd_m1 where dt='2017-05-10 00:00:00-00'),
usd_cad AS(select power(ask_o,0.091) from oanda_usd_cad_m1 where dt='2017-05-10 00:00:00-00'),
usd_sek AS(select power(ask_o,0.042) from oanda_usd_sek_m1 where dt='2017-05-10 00:00:00-00'),
usd_chf AS(select power(ask_o,0.036) from oanda_usd_chf_m1 where dt='2017-05-10 00:00:00-00')
select eur_usd.power*usd_jpy.power*gbp_usd.power*usd_cad.power*usd_sek.power*usd_chf.power*50.14348112 as ask_o  from eur_usd,usd_jpy,gbp_usd,usd_cad,usd_sek,usd_chf;

with
eur_usd AS(select power(ask_h,-0.576) from oanda_eur_usd_m1 where dt='2017-05-10 00:00:00-00'),
usd_jpy AS(select power(ask_h,0.136) from oanda_usd_jpy_m1 where dt='2017-05-10 00:00:00-00'),
gbp_usd AS(select power(ask_h,-0.119) from oanda_gbp_usd_m1 where dt='2017-05-10 00:00:00-00'),
usd_cad AS(select power(ask_h,0.091) from oanda_usd_cad_m1 where dt='2017-05-10 00:00:00-00'),
usd_sek AS(select power(ask_h,0.042) from oanda_usd_sek_m1 where dt='2017-05-10 00:00:00-00'),
usd_chf AS(select power(ask_h,0.036) from oanda_usd_chf_m1 where dt='2017-05-10 00:00:00-00')
select eur_usd.power*usd_jpy.power*gbp_usd.power*usd_cad.power*usd_sek.power*usd_chf.power*50.14348112 as ask_h from eur_usd,usd_jpy,gbp_usd,usd_cad,usd_sek,usd_chf;

with
eur_usd AS(select power(ask_l,-0.576) from oanda_eur_usd_m1 where dt='2017-05-10 00:00:00-00'),
usd_jpy AS(select power(ask_l,0.136) from oanda_usd_jpy_m1 where dt='2017-05-10 00:00:00-00'),
gbp_usd AS(select power(ask_l,-0.119) from oanda_gbp_usd_m1 where dt='2017-05-10 00:00:00-00'),
usd_cad AS(select power(ask_l,0.091) from oanda_usd_cad_m1 where dt='2017-05-10 00:00:00-00'),
usd_sek AS(select power(ask_l,0.042) from oanda_usd_sek_m1 where dt='2017-05-10 00:00:00-00'),
usd_chf AS(select power(ask_l,0.036) from oanda_usd_chf_m1 where dt='2017-05-10 00:00:00-00')
select eur_usd.power*usd_jpy.power*gbp_usd.power*usd_cad.power*usd_sek.power*usd_chf.power*50.14348112 as ask_l from eur_usd,usd_jpy,gbp_usd,usd_cad,usd_sek,usd_chf;

with
eur_usd AS(select power(ask_c,-0.576) from oanda_eur_usd_m1 where dt='2017-05-10 00:00:00-00'),
usd_jpy AS(select power(ask_c,0.136) from oanda_usd_jpy_m1 where dt='2017-05-10 00:00:00-00'),
gbp_usd AS(select power(ask_c,-0.119) from oanda_gbp_usd_m1 where dt='2017-05-10 00:00:00-00'),
usd_cad AS(select power(ask_c,0.091) from oanda_usd_cad_m1 where dt='2017-05-10 00:00:00-00'),
usd_sek AS(select power(ask_c,0.042) from oanda_usd_sek_m1 where dt='2017-05-10 00:00:00-00'),
usd_chf AS(select power(ask_c,0.036) from oanda_usd_chf_m1 where dt='2017-05-10 00:00:00-00')
select eur_usd.power*usd_jpy.power*gbp_usd.power*usd_cad.power*usd_sek.power*usd_chf.power*50.14348112 as ask_c from eur_usd,usd_jpy,gbp_usd,usd_cad,usd_sek,usd_chf;




EOF
