# -*- coding: utf-8 -*-
"""
Prints out a list that contains only the elements that
are common between the lists (without duplicates).

Created on Thu Mar  1 22:20:05 2018

@author: Abdallah Emad
"""
import random as rd
# generaring random lists containing numbers from 0-100 with random
# length
a = rd.sample(range(100), rd.randint(0,100))
b = rd.sample(range(100), rd.randint(0,100))

# assigning the lists to alises to loop throught the shortest one
y = a if len(a) < len(b) else b
z = b if y == a else a

# printing a sorted list of the elements in both lists with no
# duplicates
print(sorted(list({x for x in y if x in z})))