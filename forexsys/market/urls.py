from django.conf.urls import  include,url
from django.conf import settings
#from tradesys.views import TradePlan
from market.views import TempTableView, tt_insert, add_data_set , insert_success


urlpatterns = [
    url(r'^add/(?P<sym>\w+)/(?P<dt>\d{10})/(?P<o>\d+\.\d+)/(?P<h>\d+\.\d+)/(?P<l>\d+\.\d+)/(?P<c>\d+\.\d+)/(?P<v>\d+)/$', tt_insert),
    url(r'^new$',add_data_set),
    url(r'^add/ok$',insert_success),
]
