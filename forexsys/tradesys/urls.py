from django.conf.urls import patterns, url
from django.conf import settings
from tradesys.views import TradePlan


urlpatterns = patterns('tradesys.views',
                       url(r'^MyTradePlan/$', 'TradePlan.tp_sum_view'),
                       url(r'^MyTradePlan/market_over_view/$', 'TradePlan.market_over_view'),
                       url(r'^MyTradePlan/market_over_view/(?P<tp_id>\d+)/$', 'TradePlan.market_over_view'),
                       url(r'^MyTradePlan/market_diff_view/$', 'TradePlan.market_diff_view'),
                       url(r'^MyTradePlan/market_diff_view/(?P<tp_id>\d+)/$', 'TradePlan.market_diff_view'),
                       url(r'^MyTradePlan/first_select_view/$', 'TradePlan.first_select_view'),
                       url(r'^MyTradePlan/first_select_view/(?P<tp_id>\d+)/$', 'TradePlan.first_select_view'),
                       url(r'^MyTradePlan/analysis_selected_view/$', 'TradePlan.analysis_selected_view'),
                       url(r'^MyTradePlan/analysis_selected_view/(?P<tp_id>\d+)/$', 'TradePlan.analysis_selected_view'),
                       url(r'^MyTradePlan/tradeplan_action_view/$', 'TradePlan.tradeplan_action_view'),
                       url(r'^MyTradePlan/tradeplan_action_view/(?P<tp_id>\d+)/$', 'TradePlan.tradeplan_action_view'),
                       url(r'^MyTradePlan/report_view/(?P<tp_id>\d+)/$', 'TradePlan.report_view'),
                       #url(r'^static/(?P<path>.*)$', 'django.views.static.serve',  {'document_root': settings.STATIC_DOC_ROOT}),
                       )

