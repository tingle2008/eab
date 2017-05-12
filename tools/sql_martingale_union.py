#!/usr/bin/env  python

import sys


def main(argv):
    out_str = ' union '.join([
'select * from t_ab3c1805d178806b847caeb211e3d41c where id  %s' % argv,
'select * from t_c418fa4ea7149559365bc5bb830a0af2 where id  %s' % argv,
'select * from t_d98d8ac8d9e18c85d643cb1f4a4bb4de where id  %s' % argv,
'select * from t_3c644c569f7a39915a2b1b2264ac4ccb where id  %s' % argv,
'select * from t_ff9f637f8f014cc5338dc74e35d2eeff where id  %s' % argv,
'select * from t_dd6fc762032368206389aa665293d9e5 where id  %s' % argv,
'select * from t_e90b41adc167b1f8ac87b550917cc696 where id  %s' % argv,
'select * from t_a1235396e2f9faf84bfd7180cd58c0f9 where id  %s' % argv,
'select * from t_554626c9836b3c2bc2e98b844df000da where id  %s' % argv,
'select * from t_514b96d6d93a62497c7d4e267beef869 where id  %s' % argv,
'select * from t_ba877653bd26f6b3ada0ced5cf7afdd2 where id  %s' % argv,
'select * from t_bff2e109d7591db110e3afab05b3eedd where id  %s' % argv,
'select * from t_57ff96f5ee6fc59d7d46b8fd0d75e295 where id  %s' % argv,
'select * from t_c0bfcdacdf43922956f8c31581175f10 where id  %s' % argv,
'select * from t_b17cd334529f4a3f1bce8f8e1e77624e where id  %s' % argv,
'select * from t_dc4d81131b9158738074636fe4778589 where id  %s' % argv,
'select * from t_c1b97b98e5c76a38cb506716e73fd605 where id  %s' % argv,
'select * from t_fc0a95005e05f9aa3c6ae95d84fbeeba where id  %s' % argv,
'select * from t_d1ec431c6711d81602f51dff35ec0b39 where id  %s' % argv,
'select * from t_9ae54efea189c77014615502aa0112e6 where id  %s' % argv,
'select * from t_669a099f863fa9fcf87843e8459db7e4 where id  %s' % argv,
'select * from t_4c0e09fc3fda70362308c261e9357eb0 where id  %s' % argv,
'select * from t_f069ff17d2fe5ac9693ab632d0819e9a where id  %s' % argv,
'select * from t_8e039783886f9a83a7cc25cce316162a where id  %s' % argv,
'select * from t_9a1ed246ff8d3f54a0ceeae54fd4a974 where id  %s' % argv,
'select * from t_dd01a6b2f27a782fae7074be001980d1 where id  %s' % argv,
'select * from t_4193def7df52b9aa13ed6c629a8f9593 where id  %s' % argv,
'select * from t_2ddb3e769ad0d367ccfa5b3ddd7c75f6 where id  %s' % argv,
])

    print out_str,";"


if __name__ == "__main__":
    main(sys.argv[1])

