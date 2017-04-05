from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from market.models  import fastTable

# Create your views here.

def market_data_insert(request,sym,dt,o):

#    sym = request.GET.get('sym')
#    dt  = request.GET.get('dt')
#    o   = request.GET.get('o')
    # low        = request.GET.get('l')
    # high       = request.GET.get('h')
    # close      = request.GET.get('c')
    # volume     = request.GET.get('v')

    print (sym,dt,o)
    return HttpResponse('true')


