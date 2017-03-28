import operator
from django import forms
from django.forms.models import modelformset_factory
from django.forms.models import BaseModelFormSet
from django.forms.models import inlineformset_factory
from models import SUB_DIR,OBJ_DIR,NORMATIVE
from models import MarketDetailInfo,MarketOverView
from models import TradePlanModel,TradePlanAction
from models import TRADEFRAME,TRADETYPE,STRENGTHSCORE,PLANRESULT
from models import EXREASON


class TradePlanInitForm(forms.ModelForm):
    class Meta:
        model = TradePlanModel
        fields = ('tradeframe','tradetype')


class MarketOverViewForm(forms.ModelForm):
    market_result = forms.CharField(widget=forms.Textarea(attrs={'class':'result_text'}))
    class Meta:
        model = MarketOverView
        fields = ('market_result',)
                

class PlanResultForm(forms.ModelForm):
    class Meta:
        model  = TradePlanModel
        fields = ('plan_result',)


FirstSelectFormset  = modelformset_factory(MarketDetailInfo,
                                           extra = 0,
                                           fields = ('exclude_reason',))

SelectedFormset  = modelformset_factory(MarketDetailInfo,
                                        extra = 0,
                                        fields = ('symbol_name','timeframe','obj_dir','sub_dir'))


MovDetailInlineFormset=inlineformset_factory(MarketOverView,
                                             MarketDetailInfo,
                                             extra=0,
                                             can_delete = False,
                                             fields = ('timeframe','obj_dir','sub_dir')
                                             )


MdvDetailFormset = modelformset_factory(MarketDetailInfo,
                                        extra = 0,
                                        fields = ('symbol_name',
                                                  'timeframe',
                                                  'obj_dir',
                                                  'sub_dir',
                                                  'strength',
                                                  'normative'))


TradePlanActionFormset  = modelformset_factory(TradePlanAction,
                                               extra = 0,
                                               fields = ('symbol_name',
                                                         'trade_type',
                                                         'trade_status',
                                                         'enter_price',
                                                         'sl_price',
                                                         'tp_price',
                                                         'holding_log'))
