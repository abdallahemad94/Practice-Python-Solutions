# -*- coding: UTF-8 -*-
"""
Asks the user for a number,
Prints out a new list of all the number divisors.

@author Abdallah Emad
"""
ask = int(input('Please, enter a number: '))

print('{1} is divisable by {0}'.format(sorted([i for i in range(1,ask//2+1) if ask % i == 0]) + [ask], ask))
