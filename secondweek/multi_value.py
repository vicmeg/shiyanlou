#!/usr/bin/env python3

import time
from multiprocessing import Process,Value,Lock

def func(val,lock):
    for i in range(50):
        time.sleep(0.01)
        '''
        lock.acquire()
        val.value += 1
        lock.release()
        '''
        with lock:
            val.value += 1

def main():
    val = Value('i',0)
    lock = Lock()
    processes = [Process(target=func, args=(val,lock)) for i in range(10)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(val.value)

if __name__ == '__main__':
    for i in range(5):
        main()
