from django.conf.urls import url,include


# from django.conf.urls import patterns, include, url
# from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
               url(r'^grappelli/', include('grappelli.urls')),
               url(r'^admin/', include(admin.site.urls)),
               url(r'^accounts/', include('accounts.urls')),
               url(r'^tradesys/', include('tradesys.urls')),
               url(r'^$', RedirectView.as_view(url='/tradesys/MyTradePlan/')),
]
