#!/usr/bin/env python3
import sys

_set = set()
for arg in sys.argv[1:]:
    _set.add(arg)

print(' '.join(_set))
