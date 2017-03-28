# -*- coding: utf-8 -*-
# -*- mode: python -*-
from django.db import models
from django.forms import ModelForm
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

SYMBOL_NAME = (
    (u'EURUSD', u'EURUSD'),
    (u'GBPUSD', u'GBPUSD'),
    (u'AUDUSD', u'AUDUSD'),
    (u'JPYUSD', u'JPYUSD'),
    (u'CADUSD', u'CADUSD'),
    (u'CHFUSD', u'CHFUSD'),
    (u'AUXUSD', u'AUXUSD'),
    (u'XAGUSD', u'XAGUSD'),
    (u'USDX', u'USDX'),
    )

TIMEFRAME = (
    (5,   u'5M'),
    (15,  u'15M'),
    (60,  u'1H'),
    (240, u'4H'),
    (1440,u'1D'),
    (10080, u'1W'),
    (40320, u'1Mon'),
    )

TRADEFRAME = (
    (5, u'超短计划(以5分钟为最小交易级别)'),
    (60, u'日计划(以1小时为最小交易级别)'),
    )

OBJ_DIR = (
    (u'N', u'N/A'),
    (u'U', u'上'),
    (u'D', u'下'),
    (u'H', u'横'),
    (u'Z', u'转'),
    )

SUB_DIR = (
    (u'N', u'N/A'),
    (u'U', u'上'),
    (u'D', u'下'),
    (u'*', u'*'),
    )

TRADETYPE = (
    (u'USDX', u'美元直盘'),
    (u'AUXUSD', u'黄金'),
    (u'XAGUSD', u'白银'),
    )

TRADEACTIONTYPE = (
    (u'OP_BUY'      , u'市价买入'),
    (u'OP_SELL'     , u'市价卖出'),
    (u'OP_BUYLIMIT' , u'限价买入'),
    (u'OP_SELLLIMIT', u'限价卖出'),
    (u'OP_BUYSTOP'  , u'突破买入'),
    (u'OP_SELLSTOP' , u'突破卖出')
    )

TRADESTATUS = (
    (u'ST_PENDING'     , u'场外挂单中'),
    (u'ST_HOLDING'     , u'场内持仓中'),
    (u'ST_CANCEL'      , u'撤销挂单'),
    (u'ST_TPOUT'       , u'盈利出局'),
    (u'ST_SLOUT'       , u'亏损出局')
    )

STRENGTHSCORE = (
    (4.0, 4),
    (3.75, 3.75),
    (3.5, 3.5),
    (3.25, 3.25),
    (3.0, 3),
    (2.0,2),
    (0.0,0)
    )

PLANRESULT = (
    (u'B', u'做多'),
    (u'S', u'做空'),
    (u'G', u'进一步分析'),
    (u'N', u'不做交易'),
    )


NORMATIVE = (
    (u'NoCC',      u'暂无中继/次'),
    (u'HaveRelay', u'中继或者次'),
    (u'HaveCC',    u'不规范的次'),
    (u'1stClass',  u'一等中继模型'),
    (u'2thClass',  u'二等通道模型'),
    (u'3thClass',  u'三等反弹模型'),
    (u'MacdClass', u'MACD反弹模型'),
    (u'Double', u'双顶/底'),
    (u'H&S'   , u'头肩顶/底')
    )

EXREASON = (
    (u'N'    , u'暂无'),
    (u'多弱'  , u'做多但相对较弱'),
    (u'空强'  , u'做空但相对较强'),
    (u'看不懂', u'行情乱看不懂'),
    (u'有重要支撑阻力限制'   , u'有重要支撑阻力限制'),
    (u'macd 动能充盈不逆向交易' , u'macd 动能充盈不逆向交易')
    )

class MarketOverView(models.Model):
    market_result = models.CharField(max_length=500,blank=True)
    pub_date      = models.DateTimeField()
    def __unicode__(self):
        return '%s' % self.pub_date

class MarketDetailInfo(models.Model):
    symbol_name = models.CharField(max_length = 20,choices = SYMBOL_NAME)
    timeframe   = models.IntegerField(choices = TIMEFRAME)
    obj_dir     = models.CharField(max_length =10,choices  = OBJ_DIR)
    sub_dir     = models.CharField(max_length =10,choices  = SUB_DIR)
    strength    = models.FloatField(max_length=5,
                                    choices=STRENGTHSCORE,
                                    blank=True,
                                    null=True)
    normative   = models.CharField(max_length=20,
                                   choices=NORMATIVE,
                                   blank=True,
                                   null=True)
    exclude_reason = models.CharField(max_length = 100,
                                      choices = EXREASON,
                                      blank=True,
                                      null=True)

    market_overview = models.ForeignKey(MarketOverView)
    
    def __unicode__(self):
        return '%s %s %s %s %s @ %s' % (self.symbol_name,
                                        self.timeframe,
                                        self.obj_dir,
                                        self.sub_dir,
                                        self.exclude_reason,
                                        self.market_overview)


class TradePlanModel(models.Model):
    begin_time       = models.DateTimeField()
    end_time         = models.DateTimeField(blank=True,null=True)
    completion       = models.IntegerField()
    created_by       = models.ForeignKey(User,blank=True,null=True)
    tradeframe       = models.IntegerField(choices=TRADEFRAME,
                                        default = TRADEFRAME[1][0])
    tradetype        = models.CharField(max_length=10,
                                        choices=TRADETYPE,
                                        default = TRADETYPE[0][0]
                                        )
    #tradeplan_action = models.ForeignKey(TradePlanAction)
    # 一个TradePlan 可能会对0个或多个 TradePlanAction , 当0 个的时候表示不交易，等待下一个交易计划周期
    
    market_overview  = models.ForeignKey(MarketOverView,
                                         related_name='market_overview',
                                         # editable = False,
                                         blank=True,
                                         null=True)    
    diff_b_overview  = models.ForeignKey(MarketOverView,
                                         related_name='diff_b_overview',
                                         # editable = False,
                                         blank=True,
                                         null=True)
    diff_s_overview  = models.ForeignKey(MarketOverView,
                                         related_name='diff_s_overview',
                                         # editable = False,
                                         blank=True,
                                         null=True)
    plan_result      = models.CharField(max_length=5,choices=PLANRESULT,blank=True,null=True)

    def isOwnedBy(self, user):
        return self.created_by == user
    
    def __unicode__(self):
        return 'ID:%s | @[%s]' % (self.id,self.begin_time)

class TradePlanAction(models.Model):
    tradeplan   = models.ForeignKey(TradePlanModel)
    symbol_name = models.CharField(max_length = 20,
                                   choices = SYMBOL_NAME)
    trade_type  = models.CharField(max_length=50,
                                   choices=TRADEACTIONTYPE,
                                   blank = True,
                                   null  = True)
    trade_status= models.CharField(max_length=50,
                                   choices=TRADESTATUS,
                                   blank = True,
                                   null  = True)
    enter_price = models.FloatField()
    sl_price    = models.FloatField()
    tp_price    = models.FloatField()
    holding_log = models.CharField(max_length=5000,
                                   blank = True,
                                   null  = True)
    
    def __unicode__(self):
        return 'ID:%s | @[%s] | Action[%s]' % (self.id,self.symbol_name,self.trade_type)
    
