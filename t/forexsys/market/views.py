import json
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse

from django.db import IntegrityError
# Create your views here.

from django.views.generic.edit import CreateView
from market.models import TempTableModel
from market.forms import TempTableForm

class TempTableView(CreateView):
    form_class    = TempTableForm
    model         = TempTableModel
    template_name = "market/1mdata.html"
    success_url   = "/market/add/ok"


def save_to_temptable(sym,x):
    try:
        t = TempTableModel(dt=x['dt'],o=float(x['o']),h=float(x['h']),l=float(x['l']),c=float(x['c']),v=int(x['v']),sym=sym)
        t.save()
    except IntegrityError as e:
        if 'unique constraint' in e.message:
            print "."
        else:
            print "Error Json string"

@csrf_exempt
@api_view(['GET', 'POST'])
def add_data_set(request):
    if request.method == "POST":
        print request.data
        market = json.loads(request.data)

        for sym in  market.keys():
                map(lambda x: save_to_temptable(sym,x), market[sym])

    return HttpResponse('added')

@csrf_exempt
def tt_insert(request,sym,dt,o,h,l,c,v):
    try:
        t = TempTableModel(dt=dt,o=float(o),h=float(h),l=float(l),c=float(c),v=int(v),sym=sym)
        t.save()
    except IntegrityError as e:
        if 'unique constraint' in e.message:
            print "."
        else:
            print "Error Json string"

    return HttpResponse('tt_insert')

def insert_success(request):
    return HttpResponse('ture')


class TempTableView(CreateView):
    return HttpResponse('ture')
