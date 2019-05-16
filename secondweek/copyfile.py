#!/usr/bin/env python3
import sys

def copy_file(src,dst):
    with open(src,'r') as src_file:
        with open(dst,'w') as dst_file:
            for a,b in enumerate(src_file.readlines()):
                dst_file.write('{} {}'.format(a+1,b))
            

if __name__ == "__main__":
    copy_file(sys.argv[1], sys.argv[2])
    '''
    if len(sys.argv) == 3:
        copy_file(sys.argv[1],sys.argv[2])
        with open(sys.argv[2]) as dst_file:
                print('{} {}'.format(a+1,b))

    else:
        print("ERROR")
    sys.exit(0)
    '''
