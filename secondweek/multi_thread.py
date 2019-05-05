#!/usr/bin/env python3

import threading

def hello(name):
    print('nowxc,ID: {}'.format(threading.get_ident()))
    print('Hello ' + name)

def main():
    print('nowzhu,ID: {}'.format(threading.get_ident()))
    print('---------------------------')
    t = threading.Thread(target=hello, args=('shiyanlou',))

    t.start()
    t.join()
    print('--------------------------------')
    print('nowzhu,ID: {}'.format(threading.get_ident()))

if __name__ == '__main__':
    main()
