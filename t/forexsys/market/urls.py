from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^datainsert/$',views.market_data_insert),
    url(r'^datainsert/(?P<sym>\w+)/(?P<dt>\d{13})/(?P<o>\d+\.\d{5})/$',views.market_data_insert),
#    url(r'^datainsert/(?P<sym>\w+)/$',views.market_data_insert),
]
