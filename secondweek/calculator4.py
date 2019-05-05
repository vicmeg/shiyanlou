#!/usr/bin/env python3
# _*_coding: utf-8 _*_

import sys
import csv
import time
from multiprocessing import Process,Queue,Value,Lock,Pool

class Args:
    def __init__(self):
        l = sys.argv[1:]
        self.c = l[l.index('-c') + 1]
        self.d = l[l.index('-d') + 1]
        self.o = l[l.index('-o') + 1]

class Config:
    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        d = {'s': 0}
        with open(args.c) as f1:
            for line in f1.readlines():
                m = line.split('=')
                a,b = m[0].strip(),m[1].strip()
                if a == 'JiShuL' or a == 'JiShuH':
                    d[a] = float(b)
                else:
                    d['s'] += float(b)
        return d

def f2(q2,q1):
    for a,b in q1.get():
        salary = int(b)
        shebao = salary * config['s']
        if salary < config['JiShuL']:
            shebao = config['JiShuL'] * config['s']
        if salary > config['JiShuH']:
            shebao = config['JiShuH'] * config['s']
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
        newdata1 = [a,salary,format(shebao,'.2f'),format(tax,'.2f'),format(afterTax,'.2f')]
        time.sleep(0.01)
        newdata.append(newdata1)
    q2.put(newdata)

def f1(q1):
    with open(args.d) as f:
        data = list(csv.reader(f))
    q1.put(data)

def f3(q2):
    with open(args.o,'w') as f:
        for w in q2.get():
            csv.writer(f).writerow(w)

def main():
    Process(target=f1,args=(queue1,)).start()
    Process(target=f2,args=(queue2,queue1)).start()
    Process(target=f3,args=(queue2,)).start()

if __name__ == '__main__':
    queue1 = Queue()
    queue2 = Queue()
    args = Args()
    config = Config().config
    newdata = []
    main()