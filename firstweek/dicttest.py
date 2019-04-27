#!/usr/bin/env python3
import sys

for arg in sys.argv[1:]:
    _tuple = (arg.split(':'),)
    _dict = dict((_tuple))
    for key,value in _dict.items():
        print('ID:',key,'Name:',value)
