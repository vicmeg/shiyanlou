#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys
import csv

class Args:
    def __init__(self):
        List = sys.argv[1:]
        self.c = List[List.index('-c') + 1]
        self.d = List[List.index('-d') + 1]
        self.o = List[List.index('-o') + 1]


args = Args()

class Config:
    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        d = {'s': 0}
        with open(args.c) as f:
            for line in f.readlines():
                m = line.split('=')
                a,b = m[0].strip(),m[1].strip()
                if a == 'JiShuL' or a == 'JiShuH':
                    d[a] = float(b)
                else:
                    d['s'] += float(b)
        return d

config1 = Config().config

def calc_for_all_userdata(salary):
    salary = int(salary)
    shebao = salary * config1['s']
    if salary < config1['JiShuL']:
        shebao = config1['JiShuL'] * config1['s']
    if salary > config1['JiShuH']:
        shebao = config1['JiShuH'] * config1['s']
    m = salary - shebao - 5000
    if m <= 0:
        tax = 0
    elif m <= 3000:
        tax = m * 0.03
    elif m <= 12000:
        tax = m * 0.1 - 210
    elif m <= 25000:
        tax = m * 0.2 - 1410
    elif m <= 35000:
        tax = m * 0.25 - 2660
    elif m <= 55000:
        tax = m * 0.3 - 4410
    elif m <= 80000:
        tax = m * 0.35 - 7160
    else:
        tax = m * 0.45 - 15160
    afterTax = salary - shebao - tax
    return [salary,format(shebao,'.2f'),format(tax,'.2f'),format(afterTax,'.2f')]

class UserData:

    def __init__(self):
        with open(args.d) as f:
            l = list(csv.reader(f))
        self.value = l

data = UserData().value

with open(args.o,'w') as f:
    for a,b in data:
        x = calc_for_all_userdata(b)
        x.insert(0,a)
        csv.writer(f).writerow(x)
