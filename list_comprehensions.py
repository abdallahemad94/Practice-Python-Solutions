# -*- coding: utf-8 -*-
"""
Takes a list and makes a new list that has only the even elements of this list in it.

Created on Thu Mar  1 23:16:11 2018

@author: Abdallah Emad
"""
import random as rd
a = rd.sample(range(100), rd.randint(0,100))

print([x for x in a if x%2==0])