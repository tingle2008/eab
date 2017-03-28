from django.conf.urls import patterns, url
from accounts.views import login, logout, profile

urlpatterns = patterns('accounts',
                       url(r'^profile/$', profile),
                       url(r'^login/$', login),
                       url(r'^logout/$', logout))
