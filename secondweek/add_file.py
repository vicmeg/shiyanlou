#!/usr/bin/env python3

import os

def mk(path):
    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False

mkpath = '/home/shiyanlou/syl/A'
mkpath1 = '/home/shiyanlou/syl/B'
mkpath2 = '/home/shiyanlou/syl/C'
os.path.exists("/home/shiyanlou/syl/__init__.py")
open("/home/shiyanlou/syl/__init__.py",'w')
open("/home/shiyanlou/syl/A/__init__.py",'w')
open("/home/shiyanlou/syl/B/__init__.py",'w')
open("/home/shiyanlou/syl/C/__init__.py",'w')

mk(mkpath)
mk(mkpath1)
mk(mkpath2)
