from django.conf.urls import  include,url
from django.conf import settings
#from tradesys.views import TradePlan
from . import views


urlpatterns = [
    url(r'^add/(?P<sym>\w+)/(?P<dt>\d{13})/(?P<o>\d+\.\d+)/(?P<h>\d+\.\d+)/(?P<l>\d+\.\d+)/(?P<c>\d+\.\d+)/(?P<v>\d+)/$', views.tt_insert),
    url(r'^add/new/$',)
]

