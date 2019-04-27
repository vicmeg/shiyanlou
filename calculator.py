#!/usr/bin/env python3
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Parameter Error")
        sys.exit()
    try:
        wage = int(sys.argv[1])
    except:
        print("Parameter Error")

    ix =  wage - 5000 #ix is incomtax
    if ix <= 2100:
        print('0.00')
    elif ix > 2100 and ix <=12000:
        tax = ix * 0.1 -210
        print('{:.2f}'.format(tax))
    elif ix > 12000 and ix <= 25000:
        tax = ix * 0.2 - 1410
        print('{:.2f}'.format(tax))
    elif ix > 25000 and ix <= 35000:
        tax = ix * 0.25 - 2660
        print('{:.2f}'.format(tax))
    elif ix > 35000 and ix <= 55000:
        tax = ix * 0.3 - 4410
        print('{:.2f}'.format(tax))
    elif ix > 55000 and ix <= 80000:
        tax = ix * 0.35 - 7160
        print('{:.2f}'.format(tax))
    else:
        tax = ix * 0.45 - 15160
        print('{:.2f}'.format(tax))

