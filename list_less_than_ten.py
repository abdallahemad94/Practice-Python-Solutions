# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:26:19 2018

@author: Abdal
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
ask = int(input('Please, enter a number: '))
print([x for x in a if x < ask])