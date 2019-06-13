#!/usr/bin/env python3
import sys

output_dict = {}
def handle_data(str_):
    key,value = str_.split(':')
    output_dict[key] = value

def print_data(a,b):
    print('ID:',a,'Name:',b)

if __name__ == '__main__':

    for arg in sys.argv[1:]:
        handle_data(arg)

    for key in output_dict:
        print_data(key,output_dict[key])
