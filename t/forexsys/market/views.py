from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


from market.models import TempTable


def tt_insert(request,sym,dt,o,h,l,c,v):
    print '%s' % sym
    print '%s' % dt
    print '%s' % o
    print '%s' % h
    print '%s' % l
    print '%s' % c
    print '%s' % v

    return HttpResponse('ture')


class TempTableView(CreateView):
