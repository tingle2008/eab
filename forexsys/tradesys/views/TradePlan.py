# -*- coding: utf-8 -*-
# -*- mode: python -*-
# Create your views here.
# from tradesys.models import Symbol

import re
import os,shutil,stat
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django import forms
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.forms.formsets import formset_factory
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.generic.edit import CreateView
from tradesys.models import MarketDetailInfo,TradePlanModel,TradePlanAction
from tradesys.models import MarketOverView,TradePlanAction
from tradesys.models import SUB_DIR,OBJ_DIR,TRADEFRAME,TRADETYPE,NORMATIVE
from tradesys.models import TIMEFRAME,EXREASON
from tradesys.forms import MarketOverViewForm,PlanResultForm
from tradesys.forms import FirstSelectFormset,SelectedFormset
from tradesys.forms import MovDetailInlineFormset,TradePlanActionFormset
from tradesys.forms import TradePlanInitForm,MarketOverViewForm
from tradesys.forms import MdvDetailFormset


import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def copy_r_dir(src_dir,dst_dir):
    if not os.path.exists( dst_dir ):
        os.makedirs(dst_dir)

    for item in os.listdir(src_dir):
        subpath = os.path.join(src_dir, item)
        mode = os.stat(subpath)[stat.ST_MODE]
        if stat.S_ISDIR(mode):
            dst_path = "%s/%s" % (dst_dir,item)
            if not os.path.exists(dst_path):
                os.mkdir(dst_path)
            smgr_copy_dir(subpath,"%s/%s" % (dst_dir,item))
        elif stat.S_ISREG(mode):
            shutil.copyfile(subpath,"%s/%s" % (dst_dir,item))
        else:
            print "unkown file status and ignore it."


def trade_frame_map(tradeframe):
    if tradeframe == 5:
        return [ 5, 15, 60, 240, 1440]
    if tradeframe == 60:
        return [ 60, 240, 1440, 10080, 40320]

def tradeplan_lag_time(tradeframe):
    if tradeframe == 40320:
        return 60 * 60 * 24 * 60     # 每60天
    if tradeframe == 10080:
        return 60 * 60 * 24 * 20     # 每20天
    if tradeframe == 1440:
        return 60 * 60 * 24 * 5      # 每 5 天  
    if tradeframe == 240:            # 4 小时图
        return 60 * 60 * 32          # 32 个小时
    if tradeframe == 60:
        return 60 * 60 * 4 * 4
    if tradeframe == 15:
        return 60 * 60 * 3 
    if tradeframe == 5:
        return 60 * 60  


def sync_tradeplan_images(tp_obj):
    img_src = "%s/../full" % settings.IMAGE_ARCHIVE_DIR
    img_dst = "%s/%s" % (settings.IMAGE_ARCHIVE_DIR,tp_obj.id)
    copy_r_dir(img_src,img_dst)
    
    

def market_overview_init(request,tradetype,tradeframe):
    now    = timezone.now()
    mov = MarketOverView(market_result = "", pub_date = now)
    mov.save()

    for tf in trade_frame_map(tradeframe):

        mdi = MarketDetailInfo(symbol_name = tradetype,
                               timeframe   = tf ,
                               obj_dir     = get_prev_dir(request,tradetype,tf,'obj_dir'),
                               sub_dir     = get_prev_dir(request,tradetype,tf,'sub_dir'),
                               market_overview = mov) 
        mdi.save()
    return mov

def get_prev_dir(request,symbol,timeframe,os_dir):

    if request.session['TradePlanModel_pre_id'] is None:
        return 'N'

    prev_tp_id  = request.session['TradePlanModel_pre_id']

    prev_tp_obj = TradePlanModel.objects.get( pk = prev_tp_id )

    if symbol == prev_tp_obj.tradetype:
        mov_id  = prev_tp_obj.market_overview
    else:
        mov_id  = prev_tp_obj.diff_s_overview


    now    = timezone.now()
    lag_time = tradeplan_lag_time(timeframe)

    try:
        mdi = MarketDetailInfo.objects.get(market_overview = mov_id,
                                           timeframe = timeframe,
                                           symbol_name = symbol)
    except MarketDetailInfo.DoesNotExist:
        return 'N'

    if (now - mdi.market_overview.pub_date).total_seconds() > lag_time:
        return 'N'

    if os_dir == 'obj_dir':
        return mdi.obj_dir

    if os_dir == 'sub_dir':
        return mdi.sub_dir

    return 'N'

def diff_overview_init(request,tp_model,diff_flag):
    now = timezone.now()
    mov = MarketOverView(market_result = "", pub_date = now)
    mov.save()

    tf = trade_frame_map(tp_model.tradeframe)

    # 目前实现上主要是处理 6 个非美货币的交易
    symbols = ['EURUSD','GBPUSD','CHFUSD','AUDUSD','CADUSD','JPYUSD']

    for symbol in symbols:
        if diff_flag == 'b':
            tfm = tf[1]
            mov_save = tp_model.diff_s_overview
        if diff_flag == 's':
            tfm = tf[0]
            mov_save = mov
        mdi = MarketDetailInfo(symbol_name = symbol,
                               timeframe   = tfm ,
                               obj_dir     = get_prev_dir(request,symbol,tfm,'obj_dir'),
                               sub_dir     = get_prev_dir(request,symbol,tfm,'sub_dir'),
                               market_overview = mov_save)
        mdi.save()
    return mov

def selected_overview_init(request,tp_obj):
    try:
        selected = MarketDetailInfo.objects.filter(market_overview = tp_obj.diff_s_overview,
                                                   timeframe = tp_obj.tradeframe,
                                                   exclude_reason = 'N')
    except MarketDetailInfo.DoesNotExist:
        return False

    tfm = trade_frame_map(tp_obj.tradeframe)
    for mdi in selected:
        for tf in tfm:
            try:
                mdi_new = MarketDetailInfo.objects.get(symbol_name = mdi.symbol_name,
                                                       market_overview = tp_obj.diff_s_overview,
                                                       timeframe = tf)
            except MarketDetailInfo.DoesNotExist:
                mdi_new=MarketDetailInfo(symbol_name = mdi.symbol_name,
                                         timeframe   = tf,
                                         market_overview = tp_obj.diff_s_overview,
                                         obj_dir = 'N',
                                         sub_dir = 'N')
                mdi_new.save()


def tradeplan_action_init(tp_obj):

    selected = MarketDetailInfo.objects.filter(market_overview = tp_obj.diff_s_overview,
                                               timeframe = tp_obj.tradeframe,
                                               exclude_reason = 'N')

    exist_action = TradePlanAction.objects.filter(tradeplan = tp_obj)

    if len(exist_action) > 0:
        s = set(['%s' % x.symbol_name for x in selected ])
        e = set(['%s' % x.symbol_name for x in exist_action ])
        for sym in  e - s:
            del_tp = TradePlanAction.objects.get(tradeplan = tp_obj, symbol_name = sym)
            del_tp.delete()

    if len(selected) == 0:
        return False

    for mdi in selected:
        try:
            TradePlanAction.objects.get(symbol_name = mdi.symbol_name,
                                        tradeplan   = tp_obj)
        except TradePlanAction.DoesNotExist:
            plan_action_new=TradePlanAction(symbol_name = mdi.symbol_name,
                                            tradeplan   = tp_obj,
                                            enter_price = 0.0,
                                            sl_price    = 0.0,
                                            tp_price    = 0.0,
                                            holding_log = 'Init:')
            plan_action_new.save()


def get_selected_symbols(tradeframe,selected_overview):
    mdi = MarketDetailInfo.objects.filter(timeframe = tradeframe,
                                          exclude_reason = 'N',
                                          market_overview = selected_overview)
    if len(mdi) == 0:
        return None

    return [ '%s' % x.symbol_name for x in mdi ]


def prev_tp_id(request,tp_id):

    if tp_id is None:
        return None

    try:
        tp_obj = TradePlanModel.objects.get(pk = tp_id)
    except TradePlanModel.DoesNotExist:
        return None

    pre_tp_obj = TradePlanModel.objects.filter(created_by = request.user,
                                               tradeframe = tp_obj.tradeframe,
                                               tradetype  = tp_obj.tradetype,
                                               id__lt = tp_obj.id).order_by('-begin_time')[:1]
    if len(pre_tp_obj) == 0:
        return None
    return pre_tp_obj[0].id


def tp_id_proc(request,tp_id):

    if tp_id is not None:
        request.session['TradePlanModel_id'] = tp_id
        request.session['TradePlanModel_pre_id'] = prev_tp_id(request,tp_id)
        return tp_id

    if request.session.has_key('TradePlanModel_id'):
        request.session['TradePlanModel_pre_id'] = prev_tp_id(request,
                                                              request.session['TradePlanModel_id'])
        return request.session['TradePlanModel_id']

    # 直接访问单步骤页面的时候没有 session key 也没有 tp_id

    tp_obj =  TradePlanModel.objects
    ltp    =  tp_obj.filter(created_by = request.user).order_by('-begin_time')[:1]
    if len(ltp) == 0:
        return 'empty TradePlanModel. failed'

    request.session['TradePlanModel_id'] = ltp[0].pk
    request.session['TradePlanModel_pre_id'] = prev_tp_id(request,
                                                          request.session['TradePlanModel_id'])
    return request.session['TradePlanModel_id']


class MyTradePlanView(CreateView):
    form_class    = TradePlanInitForm
    model         = TradePlanModel
    template_name = "tradesys/MyTradePlanView.html"
    success_url   = "/tradesys/MyTradePlan/market_over_view"

    def get_context_data(self, **kwargs):
        plan_list = self.model.objects.filter(created_by=self.request.user).order_by('-begin_time')
        paginator = Paginator(plan_list, 10)
        
        page = self.request.GET.get('page')
        try:
            plans = paginator.page(page)
        except PageNotAnInteger:
            plans = paginator.page(1)
        except EmptyPage:
            plans = paginator.page(paginator.num_pages)

        context = super(MyTradePlanView, self).get_context_data(**kwargs)
        context['tradeinfo'] = TradePlanInitForm().as_ul()
        # context['oldplans'] = self.model.objects.filter(created_by=self.request.user).order_by('-begin_time')
        context['oldplans'] = plans
        return context

    def form_valid(self,form):
        if not form.is_valid():
            print "invalid from info"

        tt     =  form.cleaned_data['tradetype']
        tf     =  form.cleaned_data['tradeframe']
        user   =  self.request.user
        tp_obj =  self.model.objects
        now    = timezone.now()

        ltp = tp_obj.filter(tradeframe = tf,
                            tradetype =  tt,
                            created_by = user).order_by('-begin_time')[:1]

        lag_time = tradeplan_lag_time(tf)

        if len(ltp) == 0 or (now - ltp[0].begin_time).total_seconds() > lag_time:
            self.object = form.save(commit=False)
            self.object.begin_time = now
            self.object.completion = 1
            self.object.created_by = user
            self.object.save()

            tp_id_proc(self.request,self.object.id)
            self.object.market_overview = market_overview_init(self.request,tt,tf)
            self.object.save()

        else:
            tp_id_proc(self.request, ltp[0].id)
            self.object = ltp[0]

        sync_tradeplan_images(self.object)

        return redirect(self.success_url)

@login_required
def market_over_view(request,tp_id=None):
    
    tp_id  = tp_id_proc(request,tp_id)

    tp_obj = TradePlanModel.objects.get(pk = tp_id)

    if request.method == "POST":
        movd_formset = MovDetailInlineFormset(request.POST,
                                              request.FILES,
                                              instance = tp_obj.market_overview)
        mov_form     = MarketOverViewForm(request.POST,instance = tp_obj.market_overview)
        plan_res_form  = PlanResultForm(request.POST,instance = tp_obj)
        if movd_formset.is_valid():
            movd_formset.save()

        if mov_form.is_valid():
            mov_form.save()
        else:
            return redirect('tradesys.views.TradePlan.market_over_view')

        if plan_res_form.is_valid() and plan_res_form.cleaned_data['plan_result'] is not None:
            plan_res_form.save()
        else:
            return redirect('tradesys.views.TradePlan.market_over_view')

        if tp_obj.diff_s_overview is None:
            tp_obj.diff_s_overview = diff_overview_init(request,tp_obj,'s')
            tp_obj.save()

        if tp_obj.diff_b_overview is None:
            tp_obj.diff_b_overview = diff_overview_init(request,tp_obj,'b')
            tp_obj.save()

        if plan_res_form.cleaned_data['plan_result'] == 'N':
            return redirect('/tradesys/MyTradePlan/report_view/%d/' % tp_obj.id )

        return redirect('tradesys.views.TradePlan.market_diff_view')
    else:

        movd_formset   = MovDetailInlineFormset(instance = tp_obj.market_overview)
        mov_form       = MarketOverViewForm(instance = tp_obj.market_overview)
        plan_res_form  = PlanResultForm(instance = tp_obj)

    return render_to_response("tradesys/MarketOverView.html", {
            "tradeframe_dict" : dict(TRADEFRAME),
            "tradetype_dict" : dict(TRADETYPE),
            "timeframe_dict" : dict(TIMEFRAME),
            "tradetype" : tp_obj.tradetype,
            "movd_formset" : movd_formset,
            "mov_form" : mov_form,
            "plan_res_result" : plan_res_form,
            "image_base_url": settings.IMAGE_BASE_URL,
            },context_instance=RequestContext(request))

@login_required
def market_diff_view(request,tp_id = None):

    tp_id  = tp_id_proc(request,tp_id)
    tp_obj = TradePlanModel.objects.get(pk = tp_id)

    # usdx 是六大非美货币的交易功课.
    # 黄金/白银/交叉盘该如何设计，需要和小月月等专业人事共同设计.
    # if tp_obj.tradeytype != 'USDX':
    mdi_obj = MarketDetailInfo.objects

    s_queryset = mdi_obj.filter(market_overview = tp_obj.diff_s_overview,
                                timeframe = trade_frame_map(tp_obj.tradeframe)[0])
    b_queryset = mdi_obj.filter(market_overview = tp_obj.diff_s_overview,
                                timeframe = trade_frame_map(tp_obj.tradeframe)[1])

    if request.method == "POST":
        s_diffview = MdvDetailFormset(request.POST, request.FILES,
                                      prefix = 's',
                                      queryset = s_queryset)

        b_diffview = MdvDetailFormset(request.POST, request.FILES,
                                      prefix = 'b',
                                      queryset = b_queryset)

        mov_b_form = MarketOverViewForm(request.POST,
                                        prefix = 'b',
                                        instance = tp_obj.diff_b_overview)

        mov_s_form = MarketOverViewForm(request.POST,
                                        prefix = 's',
                                        instance = tp_obj.diff_s_overview)

        if s_diffview.is_valid():
            s_diffview.save()

        if b_diffview.is_valid():
            b_diffview.save()

        if mov_b_form.is_valid():
            mov_b_form.save()

        if mov_s_form.is_valid():
            mov_s_form.save()
        return redirect('tradesys.views.TradePlan.first_select_view')

    else:
        b_diffview = MdvDetailFormset(prefix = 'b',queryset = b_queryset)
        s_diffview = MdvDetailFormset(prefix = 's',queryset = s_queryset)
        mov_b_form =  MarketOverViewForm(prefix = 'b',instance = tp_obj.diff_b_overview)
        mov_s_form =  MarketOverViewForm(prefix = 's',instance = tp_obj.diff_s_overview)


    return render_to_response("tradesys/MarketDiffView.html", {
            "tradeframe_dict" : dict(TRADEFRAME),
            "tradetype_dict" : dict(TRADETYPE),
            "timeframe_dict" : dict(TIMEFRAME),
            "tradetype"  : tp_obj.tradetype,
            "b_diffview" : b_diffview,
            "s_diffview" : s_diffview,
            "mov_b_form" : mov_b_form,
            "mov_s_form" : mov_s_form,
            "image_base_url": settings.IMAGE_BASE_URL,
            },context_instance=RequestContext(request))


@login_required
def first_select_view(request,tp_id = None):

    tp_id = tp_id_proc(request,tp_id)
    tp_obj = TradePlanModel.objects.get(pk = tp_id)


    mdi_obj = MarketDetailInfo.objects

    s_queryset = mdi_obj.filter(market_overview = tp_obj.diff_s_overview,
                                timeframe = trade_frame_map(tp_obj.tradeframe)[0]).order_by('-symbol_name')
    mov_s_res  = tp_obj.diff_s_overview.market_result
    b_queryset = mdi_obj.filter(market_overview = tp_obj.diff_s_overview,
                                timeframe = trade_frame_map(tp_obj.tradeframe)[1]).order_by('-symbol_name')
    mov_b_res  = tp_obj.diff_b_overview.market_result

    mdi_query_set =  MarketDetailInfo.objects.filter(market_overview = tp_obj.diff_s_overview,
                                                     timeframe = tp_obj.tradeframe).order_by('-symbol_name')
    if request.method == "POST":
        first_select_view = FirstSelectFormset( request.POST,
                                                queryset = mdi_query_set )
        if first_select_view.is_valid():
            print '#' * 80
            first_select_view.save()

        selected_overview_init(request,tp_obj)

        return redirect('/tradesys/MyTradePlan/analysis_selected_view')
    else:
        first_select_view = FirstSelectFormset( queryset = mdi_query_set )

    return render_to_response("tradesys/FirstSelectView.html", {
            "tradeframe_dict" : dict(TRADEFRAME),
            "tradetype_dict" : dict(TRADETYPE),
            "timeframe_dict" : dict(TIMEFRAME),
            "sub_dir" : dict(SUB_DIR),
            "obj_dir" : dict(OBJ_DIR),
            "normative" : dict(NORMATIVE),
            "b_diffview_set" : b_queryset,
            "s_diffview_set" : s_queryset,
            "mov_b_res" : mov_b_res,
            "mov_s_res" : mov_s_res,
            "tradetype" :  tp_obj.tradetype,
            "first_select_view" : first_select_view,
            "image_base_url" : settings.IMAGE_BASE_URL,
            },context_instance=RequestContext(request))


@login_required
def report_view(request,tp_id = None):
    tp_id = tp_id_proc(request,tp_id)
    tp_obj = TradePlanModel.objects.get(pk = tp_id)

    selected = get_selected_symbols(tp_obj.tradeframe,tp_obj.diff_s_overview)
    mdi_obj = MarketDetailInfo.objects

    s_queryset = mdi_obj.filter(market_overview = tp_obj.diff_s_overview,
                                timeframe = trade_frame_map(tp_obj.tradeframe)[0]).order_by('-symbol_name')
    mov_s_res  = tp_obj.diff_s_overview.market_result
    b_queryset = mdi_obj.filter(market_overview = tp_obj.diff_s_overview,
                                timeframe = trade_frame_map(tp_obj.tradeframe)[1]).order_by('-symbol_name')
    mov_b_res  = tp_obj.diff_b_overview.market_result

    mdi_query_set =  MarketDetailInfo.objects.filter(market_overview = tp_obj.diff_s_overview,
                                                     timeframe = tp_obj.tradeframe).order_by('-symbol_name')

    movd_formset   = MovDetailInlineFormset(instance = tp_obj.market_overview)
    mov_form       = MarketOverViewForm(instance = tp_obj.market_overview)


    if selected is not None:
        selected_view = SelectedFormset(queryset = MarketDetailInfo.objects.filter(
                Q(exclude_reason = 'N'  ,market_overview = tp_obj.diff_s_overview) |
                Q(exclude_reason__isnull = True,market_overview = tp_obj.diff_s_overview),
                symbol_name__in=selected).order_by('symbol_name','-timeframe'))
        sym_count = selected_view.total_form_count()/len(trade_frame_map(tp_obj.tradeframe))
        selected = 1
    else:
        selected = 0
        selected_view = 0
        sym_count = 0

    first_select_view = FirstSelectFormset( queryset = mdi_query_set )

    return render_to_response("tradesys/ReportView.html", {
            "tradeframe_dict" : dict(TRADEFRAME),
            "tradetype_dict"  : dict(TRADETYPE),
            "timeframe_dict"  : dict(TIMEFRAME),
            "sub_dir"         : dict(SUB_DIR),
            "obj_dir"         : dict(OBJ_DIR),
            "normative"       : dict(NORMATIVE),
            "exreason"        : dict(EXREASON),
            "tp_obj"          : tp_obj,
            "movd_formset"    : movd_formset,
            "mov_form"        : mov_form,
            "b_diffview_set"  : b_queryset,
            "s_diffview_set"  : s_queryset,
            "mov_b_res"       : mov_b_res,
            "mov_s_res"       : mov_s_res,
            "tradetype"       : tp_obj.tradetype,
            "first_select_view" : first_select_view,
            "selected"        : selected,
            "timeframes"      : trade_frame_map(tp_obj.tradeframe),
            "sym_count"       : sym_count,
            "tf_count"        : len(trade_frame_map(tp_obj.tradeframe)),
            "selected_view"   : selected_view,
            "image_base_url" : settings.IMAGE_BASE_URL,
            },context_instance=RequestContext(request))

@login_required
def analysis_selected_view(request, tp_id = None):

    tp_id = tp_id_proc(request,tp_id)
    tp_obj  = TradePlanModel.objects.get(pk = tp_id)
    selected = get_selected_symbols(tp_obj.tradeframe,tp_obj.diff_s_overview)
    # 需要写入 不做交易选项. ting

    if selected is None:
        tp_obj.end_time = timezone.now()
        tp_obj.plan_result = 'N';
        tp_obj.save()
        return redirect('/tradesys/MyTradePlan/report_view/%d/' % tp_obj.id )

    if request.method == "POST":
        selected_view = SelectedFormset( request.POST,
            queryset = MarketDetailInfo.objects.filter(
                Q(exclude_reason = 'N'  ,market_overview = tp_obj.diff_s_overview) |
                Q(exclude_reason__isnull = True,market_overview = tp_obj.diff_s_overview),
                symbol_name__in=selected).order_by('symbol_name','-timeframe'))
        if selected_view.is_valid():
            selected_view.save()

        if request.POST.has_key('planresult'):
            return redirect('/tradesys/MyTradePlan/report_view/%d/' % tp_obj.id)

        tradeplan_action_init(tp_obj)

        return redirect('/tradesys/MyTradePlan/tradeplan_action_view')
    else:
        selected_view = SelectedFormset(queryset = MarketDetailInfo.objects.filter(
                Q(exclude_reason = 'N'  ,market_overview = tp_obj.diff_s_overview) |
                Q(exclude_reason__isnull = True,market_overview = tp_obj.diff_s_overview),
                symbol_name__in=selected).order_by('symbol_name','-timeframe'))

    return render_to_response("tradesys/AnalysisSelectedView.html", {
            "tradeframe_dict" : dict(TRADEFRAME),
            "tradetype_dict"  : dict(TRADETYPE),
            "timeframe_dict"  : dict(TIMEFRAME),
            "sym_count"       : selected_view.total_form_count()/len(trade_frame_map(tp_obj.tradeframe)),
            "tf_count"        : len(trade_frame_map(tp_obj.tradeframe)),
            "tradetype"       : tp_obj.tradetype,
            "timeframes"      : trade_frame_map(tp_obj.tradeframe),
            "selected_view"   : selected_view,
            "image_base_url"  : settings.IMAGE_BASE_URL,
            },context_instance=RequestContext(request))

@login_required
def tradeplan_action_view(request, tp_id = None):

    tp_id = tp_id_proc(request,tp_id)
    tp_obj  = TradePlanModel.objects.get(pk = tp_id)
    selected = get_selected_symbols(tp_obj.tradeframe,tp_obj.diff_s_overview)

    tp_action_query = TradePlanAction.objects.filter(tradeplan = tp_obj)

    if request.method == "POST":
        tradeplan_action_view = TradePlanActionFormset( request.POST,
                                                        queryset = tp_action_query)
        if tradeplan_action_view.is_valid():
            tp_obj.end_time = timezone.now()
            tp_obj.save()
            tradeplan_action_view.save()


        return redirect('/tradesys/MyTradePlan/tradeplan_action_view')
    else:
        tradeplan_action_view = TradePlanActionFormset( queryset = tp_action_query )
        selected_view = SelectedFormset(queryset = MarketDetailInfo.objects.filter(
                Q(exclude_reason = 'N'  ,market_overview = tp_obj.diff_s_overview) |
                Q(exclude_reason__isnull = True,market_overview = tp_obj.diff_s_overview),
                symbol_name__in=selected).order_by('symbol_name','-timeframe'))


    return render_to_response("tradesys/TradePlanActionView.html", {
            "tradeframe_dict" : dict(TRADEFRAME),
            "tradetype_dict" : dict(TRADETYPE),
            "timeframe_dict" : dict(TIMEFRAME),
            "tradetype" :  tp_obj.tradetype,
            "tradeplan_action_view" : tradeplan_action_view.as_ul(),
            "timeframes":  trade_frame_map(tp_obj.tradeframe),
            "selected_view" : selected_view,
            "image_base_url" : settings.IMAGE_BASE_URL,
            },context_instance=RequestContext(request))


tp_sum_view       = login_required(MyTradePlanView.as_view())


# vim: ts=4 sw=4 ai et
