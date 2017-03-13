# -*- coding:utf-8 -*-
# 用牛顿法求方程的根
import os
import math
def func(x):
    return math.pow(x,3)+4*math.pow(x,2)-10
def funcdao(x):
    return 3*math.pow(x,2)+8*x
x_temp = 1.5
x_temp_more = x_temp - func(x_temp)/funcdao(x_temp)
loop = 0
while abs(x_temp_more-x_temp) > 0.5*math.pow(10,-5):
    x_temp_more = x_temp - func(x_temp)/funcdao(x_temp)
    temp = x_temp
    x_temp =x_temp_more
    x_temp_more = temp
    print("-----")
    print(x_temp)
    print(x_temp_more)
    print("-----")
