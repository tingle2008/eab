from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/', include('accounts.urls')),
                       url(r'^tradesys/', include('tradesys.urls')),
                       url(r'^$', redirect_to, {'url': '/tradesys/MyTradePlan/'})
                       )
