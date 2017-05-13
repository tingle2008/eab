from __future__ import unicode_literals

from django.db import models
from market.models import BaseMarket

OANDA_INSTRUMNT = (
    (u'AUD_CAD',u'AUD/CAD'),
    (u'AUD_CHF',u'AUD/CHF'),
    (u'AUD_HKD',u'AUD/HKD'),
    (u'AUD_JPY',u'AUD/JPY'),
    (u'AUD_NZD',u'AUD/NZD'),
    (u'AUD_SGD',u'AUD/SGD'),
    (u'AUD_USD',u'AUD/USD'),
    (u'CAD_CHF',u'CAD/CHF'),
    (u'CAD_HKD',u'CAD/HKD'),
    (u'CAD_JPY',u'CAD/JPY'),
    (u'CAD_SGD',u'CAD/SGD'),
    (u'CHF_HKD',u'CHF/HKD'),
    (u'CHF_JPY',u'CHF/JPY'),
    (u'CHF_ZAR',u'CHF/ZAR'),
    (u'EUR_AUD',u'EUR/AUD'),
    (u'EUR_CAD',u'EUR/CAD'),
    (u'EUR_CHF',u'EUR/CHF'),
    (u'EUR_CZK',u'EUR/CZK'),
    (u'EUR_DKK',u'EUR/DKK'),
    (u'EUR_GBP',u'EUR/GBP'),
    (u'EUR_HKD',u'EUR/HKD'),
    (u'EUR_HUF',u'EUR/HUF'),
    (u'EUR_JPY',u'EUR/JPY'),
    (u'EUR_NOK',u'EUR/NOK'),
    (u'EUR_NZD',u'EUR/NZD'),
    (u'EUR_PLN',u'EUR/PLN'),
    (u'EUR_SEK',u'EUR/SEK'),
    (u'EUR_SGD',u'EUR/SGD'),
    (u'EUR_TRY',u'EUR/TRY'),
    (u'EUR_USD',u'EUR/USD'),
    (u'EUR_ZAR',u'EUR/ZAR'),
    (u'GBP_AUD',u'GBP/AUD'),
    (u'GBP_CAD',u'GBP/CAD'),
    (u'GBP_CHF',u'GBP/CHF'),
    (u'GBP_HKD',u'GBP/HKD'),
    (u'GBP_JPY',u'GBP/JPY'),
    (u'GBP_NZD',u'GBP/NZD'),
    (u'GBP_PLN',u'GBP/PLN'),
    (u'GBP_SGD',u'GBP/SGD'),
    (u'GBP_USD',u'GBP/USD'),
    (u'GBP_ZAR',u'GBP/ZAR'),
    (u'HKD_JPY',u'HKD/JPY'),
    (u'NZD_CAD',u'NZD/CAD'),
    (u'NZD_CHF',u'NZD/CHF'),
    (u'NZD_HKD',u'NZD/HKD'),
    (u'NZD_JPY',u'NZD/JPY'),
    (u'NZD_SGD',u'NZD/SGD'),
    (u'NZD_USD',u'NZD/USD'),
    (u'SGD_CHF',u'SGD/CHF'),
    (u'SGD_HKD',u'SGD/HKD'),
    (u'SGD_JPY',u'SGD/JPY'),
    (u'TRY_JPY',u'TRY/JPY'),
    (u'USD_CAD',u'USD/CAD'),
    (u'USD_CHF',u'USD/CHF'),
    (u'USD_CNH',u'USD/CNH'),
    (u'USD_CZK',u'USD/CZK'),
    (u'USD_DKK',u'USD/DKK'),
    (u'USD_HKD',u'USD/HKD'),
    (u'USD_HUF',u'USD/HUF'),
    (u'USD_INR',u'USD/INR'),
    (u'USD_JPY',u'USD/JPY'),
    (u'USD_MXN',u'USD/MXN'),
    (u'USD_NOK',u'USD/NOK'),
    (u'USD_PLN',u'USD/PLN'),
    (u'USD_SAR',u'USD/SAR'),
    (u'USD_SEK',u'USD/SEK'),
    (u'USD_SGD',u'USD/SGD'),
    (u'USD_THB',u'USD/THB'),
    (u'USD_TRY',u'USD/TRY'),
    (u'USD_ZAR',u'USD/ZAR'),
    (u'ZAR_JPY',u'ZAR/JPY'),
    (u'AU200_AUD',u'AU200/AUD'),
    (u'DE30_EUR',u'DE30/EUR'),
    (u'EU50_EUR',u'EU50/EUR'),
    (u'FR40_EUR',u'FR40/EUR'),
    (u'HK33_HKD',u'HK33/HKD'),
    (u'JP225_USD',u'JP225/USD'),
    (u'NAS100_USD',u'NAS100/USD'),
    (u'NL25_EUR',u'NL25/EUR'),
    (u'SG30_SGD',u'SG30/SGD'),
    (u'SPX500_USD',u'SPX500/USD'),
    (u'UK100_GBP',u'UK100/GBP'),
    (u'US30_USD',u'US30/USD'),
    (u'US2000_USD',u'US2000/USD'),
    (u'CN50_USD',u'CN50/USD'),
    (u'IN50_USD',u'IN50/USD'),
    (u'TWIX_USD',u'TWIX/USD'),
    (u'BCO_USD',u'BCO/USD'),
    (u'WTICO_USD',u'WTICO/USD'),
    (u'NATGAS_USD',u'NATGAS/USD'),
    (u'SOYBN_USD',u'SOYBN/USD'),
    (u'SUGAR_USD',u'SUGAR/USD'),
    (u'WHEAT_USD',u'WHEAT/USD'),
    (u'CORN_USD',u'CORN/USD'),
    (u'DE10YB_EUR',u'DE10YB/EUR'),
    (u'UK10YB_GBP',u'UK10YB/GBP'),
    (u'USB02Y_USD',u'USB02Y/USD'),
    (u'USB05Y_USD',u'USB05Y/USD'),
    (u'USB10Y_USD',u'USB10Y/USD'),
    (u'USB30Y_USD',u'USB30Y/USD'),
    (u'XAG_AUD',u'XAG/AUD'),
    (u'XAG_CAD',u'XAG/CAD'),
    (u'XAG_CHF',u'XAG/CHF'),
    (u'XAG_EUR',u'XAG/EUR'),
    (u'XAG_GBP',u'XAG/GBP'),
    (u'XAG_HKD',u'XAG/HKD'),
    (u'XAG_JPY',u'XAG/JPY'),
    (u'XAG_NZD',u'XAG/NZD'),
    (u'XAG_SGD',u'XAG/SGD'),
    (u'XAG_USD',u'XAG/USD'),
    (u'XAU_AUD',u'XAU/AUD'),
    (u'XAU_CAD',u'XAU/CAD'),
    (u'XAU_CHF',u'XAU/CHF'),
    (u'XAU_EUR',u'XAU/EUR'),
    (u'XAU_GBP',u'XAU/GBP'),
    (u'XAU_HKD',u'XAU/HKD'),
    (u'XAU_JPY',u'XAU/JPY'),
    (u'XAU_NZD',u'XAU/NZD'),
    (u'XAU_SGD',u'XAU/SGD'),
    (u'XAU_USD',u'XAU/USD'),
    (u'XAU_XAG',u'XAU/XAG'),
    (u'XPD_USD',u'XPD/USD'),
    (u'XPT_USD',u'XPT/USD'),
    (u'XCU_USD',u'XCU/USD'),
)

class AUD_CAD_M1(BaseMarket): pass
class AUD_CHF_M1(BaseMarket): pass
class AUD_HKD_M1(BaseMarket): pass
class AUD_JPY_M1(BaseMarket): pass
class AUD_NZD_M1(BaseMarket): pass
class AUD_SGD_M1(BaseMarket): pass
class AUD_USD_M1(BaseMarket): pass
class CAD_CHF_M1(BaseMarket): pass
class CAD_HKD_M1(BaseMarket): pass
class CAD_JPY_M1(BaseMarket): pass
class CAD_SGD_M1(BaseMarket): pass
class CHF_HKD_M1(BaseMarket): pass
class CHF_JPY_M1(BaseMarket): pass
class CHF_ZAR_M1(BaseMarket): pass
class EUR_AUD_M1(BaseMarket): pass
class EUR_CAD_M1(BaseMarket): pass
class EUR_CHF_M1(BaseMarket): pass
class EUR_CZK_M1(BaseMarket): pass
class EUR_DKK_M1(BaseMarket): pass
class EUR_GBP_M1(BaseMarket): pass
class EUR_HKD_M1(BaseMarket): pass
class EUR_HUF_M1(BaseMarket): pass
class EUR_JPY_M1(BaseMarket): pass
class EUR_NOK_M1(BaseMarket): pass
class EUR_NZD_M1(BaseMarket): pass
class EUR_PLN_M1(BaseMarket): pass
class EUR_SEK_M1(BaseMarket): pass
class EUR_SGD_M1(BaseMarket): pass
class EUR_TRY_M1(BaseMarket): pass
class EUR_USD_M1(BaseMarket): pass
class EUR_ZAR_M1(BaseMarket): pass
class GBP_AUD_M1(BaseMarket): pass
class GBP_CAD_M1(BaseMarket): pass
class GBP_CHF_M1(BaseMarket): pass
class GBP_HKD_M1(BaseMarket): pass
class GBP_JPY_M1(BaseMarket): pass
class GBP_NZD_M1(BaseMarket): pass
class GBP_PLN_M1(BaseMarket): pass
class GBP_SGD_M1(BaseMarket): pass
class GBP_USD_M1(BaseMarket): pass
class GBP_ZAR_M1(BaseMarket): pass
class HKD_JPY_M1(BaseMarket): pass
class NZD_CAD_M1(BaseMarket): pass
class NZD_CHF_M1(BaseMarket): pass
class NZD_HKD_M1(BaseMarket): pass
class NZD_JPY_M1(BaseMarket): pass
class NZD_SGD_M1(BaseMarket): pass
class NZD_USD_M1(BaseMarket): pass
class SGD_CHF_M1(BaseMarket): pass
class SGD_HKD_M1(BaseMarket): pass
class SGD_JPY_M1(BaseMarket): pass
class TRY_JPY_M1(BaseMarket): pass
class USD_CAD_M1(BaseMarket): pass
class USD_CHF_M1(BaseMarket): pass
class USD_CNH_M1(BaseMarket): pass
class USD_CZK_M1(BaseMarket): pass
class USD_DKK_M1(BaseMarket): pass
class USD_HKD_M1(BaseMarket): pass
class USD_HUF_M1(BaseMarket): pass
class USD_INR_M1(BaseMarket): pass
class USD_JPY_M1(BaseMarket): pass
class USD_MXN_M1(BaseMarket): pass
class USD_NOK_M1(BaseMarket): pass
class USD_PLN_M1(BaseMarket): pass
class USD_SAR_M1(BaseMarket): pass
class USD_SEK_M1(BaseMarket): pass
class USD_SGD_M1(BaseMarket): pass
class USD_THB_M1(BaseMarket): pass
class USD_TRY_M1(BaseMarket): pass
class USD_ZAR_M1(BaseMarket): pass
class ZAR_JPY_M1(BaseMarket): pass
class DE10YB_EUR_M1(BaseMarket): pass
class UK10YB_GBP_M1(BaseMarket): pass
class USB02Y_USD_M1(BaseMarket): pass
class USB05Y_USD_M1(BaseMarket): pass
class USB10Y_USD_M1(BaseMarket): pass
class USB30Y_USD_M1(BaseMarket): pass
class BCO_USD_M1(BaseMarket): pass
class WTICO_USD_M1(BaseMarket): pass
class NATGAS_USD_M1(BaseMarket): pass
class SOYBN_USD_M1(BaseMarket): pass
class SUGAR_USD_M1(BaseMarket): pass
class WHEAT_USD_M1(BaseMarket): pass
class CORN_USD_M1(BaseMarket): pass
class XAG_AUD_M1(BaseMarket): pass
class XAG_CAD_M1(BaseMarket): pass
class XAG_CHF_M1(BaseMarket): pass
class XAG_EUR_M1(BaseMarket): pass
class XAG_GBP_M1(BaseMarket): pass
class XAG_HKD_M1(BaseMarket): pass
class XAG_JPY_M1(BaseMarket): pass
class XAG_NZD_M1(BaseMarket): pass
class XAG_SGD_M1(BaseMarket): pass
class XAG_USD_M1(BaseMarket): pass
class XAU_AUD_M1(BaseMarket): pass
class XAU_CAD_M1(BaseMarket): pass
class XAU_CHF_M1(BaseMarket): pass
class XAU_EUR_M1(BaseMarket): pass
class XAU_GBP_M1(BaseMarket): pass
class XAU_HKD_M1(BaseMarket): pass
class XAU_JPY_M1(BaseMarket): pass
class XAU_NZD_M1(BaseMarket): pass
class XAU_SGD_M1(BaseMarket): pass
class XAU_USD_M1(BaseMarket): pass
class XAU_XAG_M1(BaseMarket): pass
class XPD_USD_M1(BaseMarket): pass
class XPT_USD_M1(BaseMarket): pass
class XCU_USD_M1(BaseMarket): pass
class AU200_AUD_M1(BaseMarket): pass
class DE30_EUR_M1(BaseMarket): pass
class EU50_EUR_M1(BaseMarket): pass
class FR40_EUR_M1(BaseMarket): pass
class HK33_HKD_M1(BaseMarket): pass
class JP225_USD_M1(BaseMarket): pass
class NAS100_USD_M1(BaseMarket): pass
class NL25_EUR_M1(BaseMarket): pass
class SG30_SGD_M1(BaseMarket): pass
class SPX500_USD_M1(BaseMarket): pass
class UK100_GBP_M1(BaseMarket): pass
class US30_USD_M1(BaseMarket): pass
class US2000_USD_M1(BaseMarket): pass
class CN50_USD_M1(BaseMarket): pass
class IN50_USD_M1(BaseMarket): pass
class TWIX_USD_M1(BaseMarket): pass

# Create your models here.

