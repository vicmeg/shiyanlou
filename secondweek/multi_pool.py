#!/usr/bin/env python3

import os,time,random
from multiprocessing import Pool

def task(name):
    print('rw{}start,ID: {}'.format(name,os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('rw{}end,haoshi: {:.2f}s'.format(name,(end-start)))

if __name__ == '__main__':
    print('zhu,ID: {}'.format(os.getpid()))
    print('------------------------')
    p = Pool(4)
    for i in range(1,6):
        p.apply_async(task, args=(i,))
    p.close()
    print('zijincheng...')
    p.join()
    print('-------------------------')
    print('now zhu,ID: {}'.format(os.getpid()))
