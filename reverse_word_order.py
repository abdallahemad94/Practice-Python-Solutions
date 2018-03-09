# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 19:19:27 2018

@author: Abdal
"""


def reverse(txt):
    txt = txt.split()
    return reversed(txt)


text = input('Enter a sentence: ')
print(' '.join(reverse(text)))
