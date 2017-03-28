from tradesys.models import TradePlanModel,TradePlanAction
from tradesys.models import MarketDetailInfo,MarketOverView
from django.contrib import admin



class TradePlanModelAdmin(admin.ModelAdmin):
    pass

class TradePlanActionAdmin(admin.ModelAdmin):
    pass
    

class MarketDetailInfoAdmin(admin.ModelAdmin):
    pass

class MarketOverViewAdmin(admin.ModelAdmin):
    pass


admin.site.register(TradePlanModel,TradePlanModelAdmin)
admin.site.register(TradePlanAction,TradePlanActionAdmin)
admin.site.register(MarketDetailInfo,MarketDetailInfoAdmin)
admin.site.register(MarketOverView,MarketOverViewAdmin)

