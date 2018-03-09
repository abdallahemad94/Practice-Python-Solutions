# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 18:55:32 2018

@author: Abdal
"""
import random as rd


def remove1(a_list):
    """ remove duplicates using loops"""
    b_list = []
    b_list = [i for i in a_list if i not in b_list]
    return b_list


def remove2(a_list):
    """remove duplicates using sets"""
    return set(a_list)


a_lis = rd.sample(range(0, 100), rd.randint(0, 100))
remove1(a_lis)
remove2(a_lis)
