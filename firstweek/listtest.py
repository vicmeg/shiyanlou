#!/usr/bin/env python3
import sys

short_str_list = []
long_str_list = []

for arg in sys.argv[1:]:
    if len(arg) <= 3:
        short_str_list.append(arg)
    else:
        long_str_list.append(arg)

print(' '.join(short_str_list))
print(' '.join(long_str_list))
