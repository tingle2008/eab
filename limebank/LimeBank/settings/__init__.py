# -*- coding: utf-8 -*-
import os

current_dirname = os.path.dirname(os.path.abspath(__file__))
is_production = '%s/.is_production' % current_dirname

if os.path.isfile(is_production):
    print "##" * 50
    print 
    print ' Warning: The **PRODUCTION** settings have been loaded... '
    print 
    print '##' * 50
    from production import *
else:
    print ">>" * 50
    print 
    print ' The development settings have been loaded... '
    print 
    print '>>' * 50
    from development import *

