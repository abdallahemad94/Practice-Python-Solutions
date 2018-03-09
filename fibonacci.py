# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 13:40:01 2018

@author: Abdal
"""


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


num = int(input('Please, enter a number to generate fibonacci: '))
print([fib(i) for i in range(num+1)])
