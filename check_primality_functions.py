# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 15:39:29 2018

@author: Abdal
"""
from divisors_func import divisors


def prime():
    ask = int(input('Please, enter a number: '))
    print('Your number %i is not a prime' % ask if divisors(ask)
          else 'Your number %i is a prime' % ask)


if __name__ == '__main__':
    prime()
