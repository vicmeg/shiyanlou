#!/usr/bin/env python3
import sys

for arg in sys.argv[1:]:
    a_list = [].append(arg.split(':'))
    key, value = a_list
    _dict[key] = value
        for key,value in _dict.items():
            print('ID:',key,'Name:',value)
