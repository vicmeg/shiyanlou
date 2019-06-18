#!/usr/bin/env python3
import sys

num = []
wage = []
i = 0

def calculator():

    for arg in sys.argv[1:]:
        try:
            l = arg.split(':')
            num.append(int(l[0]))
            wage.append(int(l[1]))
        except:
            print("Parameter Error")

    for i in range(len(wage)):
        w = wage[i]
        if w > 5000:
            income = w * 0.835 - 5000
            if income > 80000:
                salary = w * 0.835 - (income * 0.45 - 15160)
            elif income > 55000:
                salary = w * 0.835 - (income * 0.35 - 7160)
            elif income > 35000:
                salary = w * 0.835 - (income * 0.3 - 4410)
            elif income > 25000:
                salary = w * 0.835 - (income * 0.25 - 2660)
            elif income > 12000:
                salary = w * 0.835 - (income * 0.2 - 1410)
            elif income > 3000:
                salary = w * 0.835 - (income * 0.1 - 210)
            else:
                salary = w * 0.835 - (income * 0.03)
        else:
            salary = w * 0.835

        print("{}:{:.2f}".format(num[i],salary))

if __name__ == '__main__':
    calculator()
