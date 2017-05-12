#!/usr/bin/env  python

import sys




def main():

    sym = {
't_2ddb3e769ad0d367ccfa5b3ddd7c75f6':'USDJPY',
't_3c644c569f7a39915a2b1b2264ac4ccb':'AUDNZD',
't_4193def7df52b9aa13ed6c629a8f9593':'USDCHF',
't_4c0e09fc3fda70362308c261e9357eb0':'NZDCHF',
't_514b96d6d93a62497c7d4e267beef869':'EURCAD',
't_554626c9836b3c2bc2e98b844df000da':'EURAUD',
't_57ff96f5ee6fc59d7d46b8fd0d75e295':'EURJPY',
't_669a099f863fa9fcf87843e8459db7e4':'NZDCAD',
't_8e039783886f9a83a7cc25cce316162a':'NZDUSD',
't_9a1ed246ff8d3f54a0ceeae54fd4a974':'EURUSD',
't_9ae54efea189c77014615502aa0112e6':'GBPUSD',
't_a1235396e2f9faf84bfd7180cd58c0f9':'CHFJPY',
't_ab3c1805d178806b847caeb211e3d41c':'AUDCAD',
't_b17cd334529f4a3f1bce8f8e1e77624e':'GBPAUD',
't_ba877653bd26f6b3ada0ced5cf7afdd2':'EURCHF',
't_bff2e109d7591db110e3afab05b3eedd':'EURGBP',
't_c0bfcdacdf43922956f8c31581175f10':'EURUSD',
't_c1b97b98e5c76a38cb506716e73fd605':'GBPCHF',
't_c418fa4ea7149559365bc5bb830a0af2':'AUDCHF',
't_d1ec431c6711d81602f51dff35ec0b39':'GBPNZD',
't_d98d8ac8d9e18c85d643cb1f4a4bb4de':'AUDJPY',
't_dc4d81131b9158738074636fe4778589':'GBPCAD',
't_dd01a6b2f27a782fae7074be001980d1':'USDCAD',
't_dd6fc762032368206389aa665293d9e5':'CADCHF',
't_e90b41adc167b1f8ac87b550917cc696':'CADJPY',
't_f069ff17d2fe5ac9693ab632d0819e9a':'NZDJPY',
't_fc0a95005e05f9aa3c6ae95d84fbeeba':'GBPJPY',
't_ff9f637f8f014cc5338dc74e35d2eeff':'AUDUSD'}


    out_str = ' union '.join([
'select \'%s\' as sym,h from t_ab3c1805d178806b847caeb211e3d41c where id !=1 and id !=2' % sym['t_ab3c1805d178806b847caeb211e3d41c'],
'select \'%s\' as sym,h from t_c418fa4ea7149559365bc5bb830a0af2 where id !=1 and id !=2' % sym['t_c418fa4ea7149559365bc5bb830a0af2'],
'select \'%s\' as sym,h from t_d98d8ac8d9e18c85d643cb1f4a4bb4de where id !=1 and id !=2' % sym['t_d98d8ac8d9e18c85d643cb1f4a4bb4de'],
'select \'%s\' as sym,h from t_3c644c569f7a39915a2b1b2264ac4ccb where id !=1 and id !=2' % sym['t_3c644c569f7a39915a2b1b2264ac4ccb'],
'select \'%s\' as sym,h from t_ff9f637f8f014cc5338dc74e35d2eeff where id !=1 and id !=2' % sym['t_ff9f637f8f014cc5338dc74e35d2eeff'],
'select \'%s\' as sym,h from t_dd6fc762032368206389aa665293d9e5 where id !=1 and id !=2' % sym['t_dd6fc762032368206389aa665293d9e5'],
'select \'%s\' as sym,h from t_e90b41adc167b1f8ac87b550917cc696 where id !=1 and id !=2' % sym['t_e90b41adc167b1f8ac87b550917cc696'],
'select \'%s\' as sym,h from t_a1235396e2f9faf84bfd7180cd58c0f9 where id !=1 and id !=2' % sym['t_a1235396e2f9faf84bfd7180cd58c0f9'],
'select \'%s\' as sym,h from t_554626c9836b3c2bc2e98b844df000da where id !=1 and id !=2' % sym['t_554626c9836b3c2bc2e98b844df000da'],
'select \'%s\' as sym,h from t_514b96d6d93a62497c7d4e267beef869 where id !=1 and id !=2' % sym['t_514b96d6d93a62497c7d4e267beef869'],
'select \'%s\' as sym,h from t_ba877653bd26f6b3ada0ced5cf7afdd2 where id !=1 and id !=2' % sym['t_ba877653bd26f6b3ada0ced5cf7afdd2'],
'select \'%s\' as sym,h from t_bff2e109d7591db110e3afab05b3eedd where id !=1 and id !=2' % sym['t_bff2e109d7591db110e3afab05b3eedd'],
'select \'%s\' as sym,h from t_57ff96f5ee6fc59d7d46b8fd0d75e295 where id !=1 and id !=2' % sym['t_57ff96f5ee6fc59d7d46b8fd0d75e295'],
'select \'%s\' as sym,h from t_c0bfcdacdf43922956f8c31581175f10 where id !=1 and id !=2' % sym['t_c0bfcdacdf43922956f8c31581175f10'],
'select \'%s\' as sym,h from t_b17cd334529f4a3f1bce8f8e1e77624e where id !=1 and id !=2' % sym['t_b17cd334529f4a3f1bce8f8e1e77624e'],
'select \'%s\' as sym,h from t_dc4d81131b9158738074636fe4778589 where id !=1 and id !=2' % sym['t_dc4d81131b9158738074636fe4778589'],
'select \'%s\' as sym,h from t_c1b97b98e5c76a38cb506716e73fd605 where id !=1 and id !=2' % sym['t_c1b97b98e5c76a38cb506716e73fd605'],
'select \'%s\' as sym,h from t_fc0a95005e05f9aa3c6ae95d84fbeeba where id !=1 and id !=2' % sym['t_fc0a95005e05f9aa3c6ae95d84fbeeba'],
'select \'%s\' as sym,h from t_d1ec431c6711d81602f51dff35ec0b39 where id !=1 and id !=2' % sym['t_d1ec431c6711d81602f51dff35ec0b39'],
'select \'%s\' as sym,h from t_9ae54efea189c77014615502aa0112e6 where id !=1 and id !=2' % sym['t_9ae54efea189c77014615502aa0112e6'],
'select \'%s\' as sym,h from t_669a099f863fa9fcf87843e8459db7e4 where id !=1 and id !=2' % sym['t_669a099f863fa9fcf87843e8459db7e4'],
'select \'%s\' as sym,h from t_4c0e09fc3fda70362308c261e9357eb0 where id !=1 and id !=2' % sym['t_4c0e09fc3fda70362308c261e9357eb0'],
'select \'%s\' as sym,h from t_f069ff17d2fe5ac9693ab632d0819e9a where id !=1 and id !=2' % sym['t_f069ff17d2fe5ac9693ab632d0819e9a'],
'select \'%s\' as sym,h from t_8e039783886f9a83a7cc25cce316162a where id !=1 and id !=2' % sym['t_8e039783886f9a83a7cc25cce316162a'],
'select \'%s\' as sym,h from t_9a1ed246ff8d3f54a0ceeae54fd4a974 where id !=1 and id !=2' % sym['t_9a1ed246ff8d3f54a0ceeae54fd4a974'],
'select \'%s\' as sym,h from t_dd01a6b2f27a782fae7074be001980d1 where id !=1 and id !=2' % sym['t_dd01a6b2f27a782fae7074be001980d1'],
'select \'%s\' as sym,h from t_4193def7df52b9aa13ed6c629a8f9593 where id !=1 and id !=2' % sym['t_4193def7df52b9aa13ed6c629a8f9593'],
'select \'%s\' as sym,h from t_2ddb3e769ad0d367ccfa5b3ddd7c75f6 where id !=1 and id !=2' % sym['t_2ddb3e769ad0d367ccfa5b3ddd7c75f6'],
])

    print out_str,";"


if __name__ == "__main__":
    main()

