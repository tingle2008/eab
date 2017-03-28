from django.conf.urls import url, include
from accounts.views import login, logout, profile

urlpatterns = [
    url(r'^profile/$', profile),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
]
