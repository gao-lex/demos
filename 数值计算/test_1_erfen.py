# -*- coding:utf-8 -*-
# 用二分法求方程的根
import os
import math
def func(x):
    return math.pow(x,3)+4*math.pow(x,2)-10
a = 1.0
b = 2.0
loop = 1

while (b-a)/2>0.5*math.pow(10,-5):
    xn = (a+b)/2
    print("a="+str(a)+'\n'+"b="+str(b)+'\n'+"xn="+str(xn)+'\n'+"n="+str(loop)+'\n'+"f(xn)"+str(func(xn)))
    if func(xn) == 0:
        os._exit()
    elif func(a)*func(xn) < 0:
        b = xn
    else:
        a = xn
    loop=loop+1