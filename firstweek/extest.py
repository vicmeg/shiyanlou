#!/usr/bin/env python3

num = input("Enter number:")

try:
    new_num = int(num)
    print('TNT:{}'.format(new_num))
except:
    print('ERROR:',num)

