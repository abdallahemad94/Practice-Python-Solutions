# -*- coding: UTF-8 -*-
"""
A program that asks the user for thier name and age,
and prints out a message addressed to them that tells them
the year that they will turn 100 years old

@author Abdalla Emad
"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
age_def = 100 - age

print("Hey " + name + " you will turn 100 in " + str(2018 + age_def))
