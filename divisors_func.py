# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 15:54:18 2018

@author: Abdal
"""


def divisors(x):
    return True if x == 1 or x == 2 else\
        sorted([i for i in range(2, x//2+1) if x % i == 0])


if __name__ == '__main__':
    divisors(5)
