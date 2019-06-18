#!/usr/bin/env python3

import sys

for arg in sys.argv[1:]:
    if len(arg) > 3:
        print(arg)
