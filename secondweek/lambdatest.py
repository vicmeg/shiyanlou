#!/usr/bin/env python3

list1 = [('Shi',100),('Yan',75),('Lou',200),('Plus',80)]

sortedlist = sorted(list1,key=lambda n: n[1])

print(sortedlist)
